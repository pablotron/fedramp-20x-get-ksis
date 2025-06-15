# import system libraries
import gzip, json, os, sys

# absolute path to base directory
BASE_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..')

# add base path to search path, import ksihtml library
sys.path.append(BASE_PATH)
import ksihtml

def test_parse():
  """test ksihtml.parse()"""
  # read expected json from "../ksis.json"
  exp = open(os.path.join(BASE_PATH, 'ksis.json')).read()

  # read html from "./index.html.gz", parse as ksis
  ksis = ksihtml.parse(gzip.open(os.path.join(BASE_PATH, 'test', 'index.html.gz')).read())

  # encode ksis as json and append newline
  got = json.dumps({"version": ksihtml.SCHEMA_VERSION, "ksis": ksis}) + "\n"

  # assert that generated json matches expected json
  assert(got == exp)
