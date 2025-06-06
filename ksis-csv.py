#!/usr/bin/env python3

#
# ksis-csv.py: Read JSON-formatted KSIs from standard input and
# write a CSV of KSIs on standard output.
#
# Example:
#
#   # generate ksis.csv from ksis.json
#   $ ksis-csv.py < ksis.json > ksis.csv
#

# load libraries
import csv, json, sys

def make_reqs(reqs: list[dict]) -> str:
  """Serialize list of validation requirements as string."""
  return "\n".join([f"{req['id']:02}: {req['text']}" for req in reqs])

# create csv writer, write column names
w = csv.writer(sys.stdout)
w.writerow(['ID', 'Name', 'Description', 'Validation'])

# read json from stdin, write csv rows to stdout
for ksi in (json.load(sys.stdin))['ksis']:
  w.writerow([ksi['id'], ksi['name'], ksi['text'], make_reqs(ksi['reqs'])])
