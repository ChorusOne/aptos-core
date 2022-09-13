#!/usr/bin/env python3

# Note: This script won't work outside of Unix since I'm just calling out
# to Unix shell commands.

# After running this, you can see detailed results at the following directory:
# {args.working_dir}/Test/RestlerResults/experiment<number>/logs/

# todo explain that you shouldn't need to alter the config files on a per run basis

import argparse
import logging
import os
import subprocess
import enum


LOG = logging.getLogger(__name__)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
ch = logging.StreamHandler()
ch.setFormatter(formatter)
LOG.addHandler(ch)


# Working directory inside the container.
CONTAINER_WORKING_DIR = "/working"


def run_command(command):
    if isinstance(command, list):
        shell = False
        LOG.debug(f"Running command: {' '.join(command)}")
    else:
        shell = True
        LOG.debug(f"Running command: {command}")

    subprocess.run(command, shell=shell)


# The `mounts` argument is a map of source host paths to in-container destination paths.
def get_docker_command(
    args, restler_subcommand=None, mounts=None, workdir=None, use_host_network=False
):
    restler_subcommand = restler_subcommand or []
    mounts = mounts or {}

    command = [
        "docker",
        "run",
        "--rm",
        "-t",
    ]

    if workdir:
        command += ["--workdir", workdir]

    if use_host_network:
        command += ["--network", "host"]

    for source, destination in mounts.items():
        command += [
            "--mount",
            f"type=bind,source={os.path.realpath(source)},target={destination}",
        ]

    command += [args.restler_image, "dotnet", "/RESTler/restler/Restler.dll"]

    command += restler_subcommand

    return command


def compile(args):
    if args.clean:
        run_command(["rm", "-rf", os.path.join(args.output_dir, "Compile")])
        run_command(["rm", "-rf", os.path.join(args.output_dir, "RestlerLogs")])

    # We have to set the workdir to the output path because the tool doesn't
    # let you set the output path directly.
    in_container_spec_path = "/spec.yaml"
    in_container_output_path = "/output"
    run_command(
        get_docker_command(
            args,
            restler_subcommand=[
                "compile",
                "--api_spec",
                in_container_spec_path,
            ],
            mounts={
                # Mounting the spec into the container.
                args.spec_path: in_container_spec_path,
                # Mounting the output dir into the container.
                args.output_dir: in_container_output_path,
            },
            workdir=in_container_output_path,
        )
    )

    LOG.info(f"Configs generated in {args.output_dir}")


# todo explain how this wraps test, fuzz-lean, and fuzz
def test(args):
    # Validate the IP.
    if args.ip.startswith("http"):
        raise ValueError(
            "IP should not start with http(s)://, use just the IP and configure "
            "https with the --ssl flag"
        )

    # Confirm the config files are there.
    grammar_file = "grammar.py"
    dict_file = "dict.json"
    engine_settings_file = "engine_settings.json"

    for file in [grammar_file, dict_file, engine_settings_file]:
        if not os.path.exists(os.path.join(args.config_dir, file)):
            raise FileNotFoundError(f"Config file not found: {file}")

    run_command(["rm", "-rf", args.output_dir])
    run_command(["mkdir", "-p", args.output_dir])

    in_container_config_path = "/config"
    in_container_results_path = "/results"

    grammar_path = os.path.join(in_container_config_path, grammar_file)
    dict_path = os.path.join(in_container_config_path, dict_file)
    engine_settings_path = os.path.join(in_container_config_path, engine_settings_file)

    restler_subcommand = [
        args.suite.get_subcommand(),
        "--grammar_file",
        grammar_path,
        "--dictionary_file",
        dict_path,
        "--settings",
        engine_settings_path,
        "--target_ip",
        args.ip,
        "--target_port",
        str(args.port),
    ]

    if not args.ssl:
        restler_subcommand += [
            "--no_ssl",
        ]

    if args.num_hours and args.suite == FuzzSuite.FULL:
        restler_subcommand += [
            "--time_budget",
            str(args.num_hours),
        ]

    run_command(
        get_docker_command(
            args,
            restler_subcommand=restler_subcommand,
            mounts={
                # Mounting the config dir into the container.
                args.config_dir: in_container_config_path,
                # Mounting the output dir into the container.
                args.output_dir: in_container_results_path,
            },
            use_host_network=True,
            workdir=in_container_results_path,
        )
    )

    LOG.info(f"Results written to {args.output_dir}")


class FuzzSuite(enum.Enum):
    BASIC = "basic"
    LEAN = "lean"
    FULL = "full"

    def get_subcommand(self):
        # Not using match statement since many folks don't have >= 3.10 as their
        # default Python3 version.
        return {
            FuzzSuite.BASIC: "test",
            FuzzSuite.LEAN: "fuzz-lean",
            FuzzSuite.FULL: "fuzz",
        }[self]


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug", action="store_true")
    parser.add_argument(
        "--working-dir", default="/tmp/aptos_api_fuzzing", help="Default: %(default)s"
    )
    parser.add_argument(
        "--restler-image",
        default="mcr.microsoft.com/restlerfuzzer/restler:v9.0.1",
        help="Default: %(default)s",
    )

    subparsers = parser.add_subparsers(required=True, dest="subcommand")

    # Compile subcommand.
    compile_parser = subparsers.add_parser(
        "compile",
        help=(
            "Compile the API spec into a grammar and config files. You should "
            "only need to run this when the API spec changes. If you do, you need "
            "to make sure you don't overwrite previous config params, as these "
            "config files are used to help RESTler generate appropriate requests. "
            "See this link for more: "
            "https://github.com/microsoft/restler-fuzzer/blob/4c691f38960f49f0a4e6110fcad8165007e7fa47/docs/user-guide/Compiling.md.",
        ),
    )
    compile_parser.set_defaults(func=compile)
    compile_parser.add_argument(
        "--spec-path", default="api/doc/spec.yaml", help="Default: %(default)s"
    )
    compile_parser.add_argument(
        "--output-dir", default="api/fuzzing", help="Default: %(default)s"
    )
    compile_parser.add_argument(
        "--clean",
        action="store_true",
        help="Wipe the generated data from the output dir before doing anything",
    )

    # Fuzz subcommand. This covers test, fuzz-lean, and fuzz in the underlying tool.
    fuzz_parser = subparsers.add_parser(
        "fuzz",
        help=(
            "This function helps you initially test the fuzzer, it doesn't do any "
            "extensive fuzzing itself. See this link for more: "
            "https://github.com/microsoft/restler-fuzzer/blob/4c691f38960f49f0a4e6110fcad8165007e7fa47/docs/user-guide/Testing.md.",
        ),
    )
    fuzz_parser.set_defaults(func=test)
    fuzz_parser.add_argument(
        "--config-dir",
        default="api/fuzzing/Compile",
        help="Directory containing the config files generated by the compile subcommand. Default: %(default)s",
    )
    fuzz_parser.add_argument(
        "--ip",
        # Even with "--network host", 127.0.0.1 doesn't refer to localhost
        # on the host, we have to do this instead.
        default="host.docker.internal",
        help="IP of the node to test. Do not include a scheme (e.g. http://). Default: %(default)s",
    )
    fuzz_parser.add_argument(
        "--port",
        type=int,
        default=8080,
        help="Port the node API is running on. Default: %(default)s",
    )
    fuzz_parser.add_argument(
        "--ssl", action="store_true", help="Use SSL when connecting to the server"
    )
    fuzz_parser.add_argument(
        "--suite",
        type=str,
        choices=[v.name.lower() for v in FuzzSuite],
        default=FuzzSuite.BASIC,
    )
    fuzz_parser.add_argument(
        "--output-dir",
        default="/tmp/api_fuzzing_results",
        help="Where to output the results. Default: %(default)s",
    )
    fuzz_parser.add_argument(
        "--num-hours",
        default=2,
        type=int,
        help='Number of hours to run. Only relevant for the "full" suite. Default: %(default)s',
    )

    args = parser.parse_args()

    if hasattr(args, "suite"):
        args.suite = FuzzSuite[args.suite.upper()]

    return args


def main():
    args = parse_args()
    print(args)

    # Set up logger.
    if args.debug:
        LOG.setLevel("DEBUG")
    else:
        LOG.setLevel("INFO")

    # Call subcommand.
    args.func(args)


if __name__ == "__main__":
    main()
