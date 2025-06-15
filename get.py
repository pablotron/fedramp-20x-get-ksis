#!/usr/bin/env python3

#
# get.py: Scrape HTML-formatted Key Security Indicators (KSIs) from
# fedramp.gov, parse them, and print JSON-encoded list of KSIs to
# standard output.
#
# Usage:
#   # get KSIs from fedramp.gov and save them to `ksis.json`
#   ./get.py > ./ksis.json
#

import json, ksihtml, requests

# fetch html, parse ksis
ksis = ksihtml.parse(requests.get(ksihtml.URL).text)

# json-encode ksis, print to stdout
print(json.dumps({"version": ksihtml.SCHEMA_VERSION, "ksis": ksis}))
