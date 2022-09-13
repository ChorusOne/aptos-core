// Copyright (c) Aptos
// SPDX-License-Identifier: Apache-2.0

use crate::{LoadDestination, NetworkLoadTest};
use forge::{
    GroupNetworkDelay, NetworkContext, NetworkTest, Swarm, SwarmChaos, SwarmExt, SwarmNetworkDelay,
    Test,
};

pub struct NetworkLatencyTest;

impl Test for NetworkLatencyTest {
    fn name(&self) -> &'static str {
        "network::latency-test"
    }
}

fn create_three_region_swarm_network_delay(swarm: &dyn Swarm) -> SwarmNetworkDelay {
    let num_nodes = swarm.get_validator_clients_with_names().len() as u64;
    let num_nodes_per_region = num_nodes / 3;

    // baseline region has 0 latency
    let region_b = GroupNetworkDelay {
        num_nodes: num_nodes_per_region,
        latency_ms: 100,
        jitter_ms: 100,
        correlation_percentage: 10,
    };
    let region_c = GroupNetworkDelay {
        num_nodes: num_nodes_per_region,
        latency_ms: 200,
        jitter_ms: 100,
        correlation_percentage: 10,
    };
    SwarmNetworkDelay {
        group_network_delays: vec![region_b, region_c],
        num_nodes,
    }
}

impl NetworkLoadTest for NetworkLatencyTest {
    fn setup(&self, ctx: &mut NetworkContext) -> anyhow::Result<LoadDestination> {
        let delay = create_three_region_swarm_network_delay(ctx.swarm());
        let chaos = SwarmChaos::Delay(delay.clone());
        ctx.swarm().inject_chaos(chaos)?;
        let msg = format!("Injected {}", delay);
        println!("{}", msg);
        ctx.report.report_text(msg);
        Ok(LoadDestination::AllNodes)
    }

    fn finish(&self, swarm: &mut dyn Swarm) -> anyhow::Result<()> {
        let chaos = SwarmChaos::Delay(create_three_region_swarm_network_delay(swarm));
        swarm.remove_chaos(chaos)
    }
}

impl NetworkTest for NetworkLatencyTest {
    fn run<'t>(&self, ctx: &mut NetworkContext<'t>) -> anyhow::Result<()> {
        <dyn NetworkLoadTest>::run(self, ctx)
    }
}
