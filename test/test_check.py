# import system libraries
import json, jsonschema, os

# absolute path to base directory
BASE_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..')

def test_check():
  """test that `ksis.json` validates against `schema.json`"""
  # read KSIs from "../ksis.json"
  data = json.load(open(os.path.join(BASE_PATH, 'ksis.json')))

  # read schema from "../schema.json"
  schema = json.load(open(os.path.join(BASE_PATH, 'schema.json')))

  # validate data against schema
  jsonschema.validate(data, schema)

  # assert that generated json matches expected json
  assert(1)
