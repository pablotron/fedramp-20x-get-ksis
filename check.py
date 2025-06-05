#!/usr/bin/env python3

#
# check.py: Validate KSIs JSON against schema.
#
# Usage:
#
#   # validate ksis.json against JSON schema
#   ./check.py < ksis.json
#

# load libraries
import json, jsonschema, os, sys

# absolute path to JSON schema file (./schema.json)
SCHEMA_PATH = os.path.join(os.path.dirname(__file__), 'schema.json')

# load JSON schema
with open(SCHEMA_PATH) as f:
  schema = json.load(f)

# read json data from stdin
data = json.load(sys.stdin)

# validate JSON against schema
jsonschema.validate(data, schema)
print("ok")
