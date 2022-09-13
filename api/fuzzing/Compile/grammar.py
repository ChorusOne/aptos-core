""" THIS IS AN AUTOMATICALLY GENERATED FILE!"""
from __future__ import print_function
import json
from engine import primitives
from engine.core import requests
from engine.errors import ResponseParsingException
from engine import dependencies
req_collection = requests.RequestCollection([])
# Endpoint: /accounts/{address}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("accounts"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("ledger_version="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["32425224034"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/accounts/{address}"
)
req_collection.add_request(request)

# Endpoint: /accounts/{address}/resources, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("accounts"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("resources"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("ledger_version="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["32425224034"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/accounts/{address}/resources"
)
req_collection.add_request(request)

# Endpoint: /accounts/{address}/modules, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("accounts"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("modules"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("ledger_version="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["32425224034"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/accounts/{address}/modules"
)
req_collection.add_request(request)

# Endpoint: /spec, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("spec"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/spec"
)
req_collection.add_request(request)

# Endpoint: /-/healthy, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("-"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("healthy"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("duration_secs="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/-/healthy"
)
req_collection.add_request(request)

# Endpoint: /blocks/by_height/{block_height}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("blocks"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("by_height"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("with_transactions="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/blocks/by_height/{block_height}"
)
req_collection.add_request(request)

# Endpoint: /blocks/by_version/{version}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("blocks"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("by_version"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("with_transactions="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/blocks/by_version/{version}"
)
req_collection.add_request(request)

# Endpoint: /events/{event_key}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("events"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("start="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["32425224034"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/events/{event_key}"
)
req_collection.add_request(request)

# Endpoint: /accounts/{address}/events/{creation_number}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("accounts"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("events"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("start="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["32425224034"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/accounts/{address}/events/{creation_number}"
)
req_collection.add_request(request)

# Endpoint: /accounts/{address}/events/{event_handle}/{field_name}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("accounts"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("events"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("start="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["32425224034"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/accounts/{address}/events/{event_handle}/{field_name}"
)
req_collection.add_request(request)

# Endpoint: , method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId=""
)
req_collection.add_request(request)

# Endpoint: /accounts/{address}/resource/{resource_type}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("accounts"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("resource"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("ledger_version="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["32425224034"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/accounts/{address}/resource/{resource_type}"
)
req_collection.add_request(request)

# Endpoint: /accounts/{address}/module/{module_name}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("accounts"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("module"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("ledger_version="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["32425224034"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/accounts/{address}/module/{module_name}"
)
req_collection.add_request(request)

# Endpoint: /tables/{table_handle}/item, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tables"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("item"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("ledger_version="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["32425224034"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "key_type":
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
    ,
    "value_type":
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
    ,
    "key":
        """),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("""
    }"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/tables/{table_handle}/item"
)
req_collection.add_request(request)

# Endpoint: /transactions, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("transactions"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("start="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["32425224034"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/transactions"
)
req_collection.add_request(request)

# Endpoint: /transactions, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("transactions"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "sender":
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["0x88fbd33f54e1126269769780feb24480428179f552e2313fbe571b72e62a1ca1 "]),
    primitives.restler_static_string("""
    ,
    "sequence_number":
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["32425224034"]),
    primitives.restler_static_string("""
    ,
    "max_gas_amount":
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["32425224034"]),
    primitives.restler_static_string("""
    ,
    "gas_unit_price":
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["32425224034"]),
    primitives.restler_static_string("""
    ,
    "expiration_timestamp_secs":
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["32425224034"]),
    primitives.restler_static_string("""
    ,
    "payload":
        """),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("""
    ,
    "signature":
        """),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("""
    }"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/transactions"
)
req_collection.add_request(request)

# Endpoint: /transactions/by_hash/{txn_hash}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("transactions"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("by_hash"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/transactions/by_hash/{txn_hash}"
)
req_collection.add_request(request)

# Endpoint: /transactions/by_version/{txn_version}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("transactions"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("by_version"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/transactions/by_version/{txn_version}"
)
req_collection.add_request(request)

# Endpoint: /accounts/{address}/transactions, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("accounts"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("transactions"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("start="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["32425224034"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/accounts/{address}/transactions"
)
req_collection.add_request(request)

# Endpoint: /transactions/batch, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("transactions"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("batch"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("["),
    primitives.restler_static_string("""
    {
        "sender":
            "0x88fbd33f54e1126269769780feb24480428179f552e2313fbe571b72e62a1ca1 "
        ,
        "sequence_number":
            "32425224034"
        ,
        "max_gas_amount":
            "32425224034"
        ,
        "gas_unit_price":
            "32425224034"
        ,
        "expiration_timestamp_secs":
            "32425224034"
        ,
        "payload":
            """),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("""
        ,
        "signature":
            """),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("""
    }]"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/transactions/batch"
)
req_collection.add_request(request)

# Endpoint: /transactions/simulate, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("transactions"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("simulate"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "sender":
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["0x88fbd33f54e1126269769780feb24480428179f552e2313fbe571b72e62a1ca1 "]),
    primitives.restler_static_string("""
    ,
    "sequence_number":
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["32425224034"]),
    primitives.restler_static_string("""
    ,
    "max_gas_amount":
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["32425224034"]),
    primitives.restler_static_string("""
    ,
    "gas_unit_price":
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["32425224034"]),
    primitives.restler_static_string("""
    ,
    "expiration_timestamp_secs":
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["32425224034"]),
    primitives.restler_static_string("""
    ,
    "payload":
        """),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("""
    ,
    "signature":
        """),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("""
    }"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/transactions/simulate"
)
req_collection.add_request(request)

# Endpoint: /transactions/encode_submission, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("transactions"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("encode_submission"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "sender":
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["0x88fbd33f54e1126269769780feb24480428179f552e2313fbe571b72e62a1ca1 "]),
    primitives.restler_static_string("""
    ,
    "sequence_number":
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["32425224034"]),
    primitives.restler_static_string("""
    ,
    "max_gas_amount":
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["32425224034"]),
    primitives.restler_static_string("""
    ,
    "gas_unit_price":
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["32425224034"]),
    primitives.restler_static_string("""
    ,
    "expiration_timestamp_secs":
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["32425224034"]),
    primitives.restler_static_string("""
    ,
    "payload":
        """),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("""
    ,
    "secondary_signers":
    [
        "0x88fbd33f54e1126269769780feb24480428179f552e2313fbe571b72e62a1ca1 "
    ]}"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/transactions/encode_submission"
)
req_collection.add_request(request)

# Endpoint: /estimate_gas_price, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("estimate_gas_price"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: \r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/estimate_gas_price"
)
req_collection.add_request(request)
