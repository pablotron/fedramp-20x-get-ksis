#!/usr/bin/env python3

#
# check.py: Validate JSON of KSIs against JSON schema.
#
# If validation passes, then this script prints "ok" to standard output
# and returns an exit code of 0.
#
# If validation fails, then this script prints the validation errors to
# standard error and returns a non-zero exit code.
#
# Usage:
#
#   # check "ksis.json" against JSON schema
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
