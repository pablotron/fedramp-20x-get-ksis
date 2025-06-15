"""Scraper for FedRAMP 20x KSIs"""

import bs4, re

# Fedramp KSIs URL
URL = 'https://www.fedramp.gov/20x/standards/20x-ksi/'

# Schema version
SCHEMA_VERSION = '20250605'

def next_p(e: bs4.Tag) -> bs4.Tag|None:
  """skip to next sibling <p> in this section or return None"""
  while e is not None and e.name != 'p':
    if e.name == 'h2':
      return None # beginning of next section
    e = e.next_element
  return e

def make_ksi(h2: bs4.Tag) -> dict:
  """create KSI dict from KSI <h2> title element and <p> sibling elements"""
  e = next_p(h2.next_element) # skip to next <p>

  ksi_id = e.select('strong')[0].text.replace(':', '') # ksi id
  text = e.contents[1].text.strip() # ksi description
  name = h2.text # ksi name
  e = next_p(e.next_element) # skip description
  e = next_p(e.next_element) # skip validation blurb

  # get validation requirements
  reqs = []
  while e is not None:
    md = re.match(r"([0-9]+): +(.+)", e.text.strip()) # match req id/text
    if md is not None:
      reqs.append({ "id": int(md[1]), "text": md[2] }) # append req
    e = next_p(e.next_element) # skip to next <p>

  # build/return ksi dict
  return { "id": ksi_id, "text": text, "name": name, "reqs": reqs }

def parse(data: str) -> list[dict]:
  """Parse HTML into list of KSIs."""
  doc = bs4.BeautifulSoup(data, 'lxml') # parse html
  return [make_ksi(h2) for h2 in doc.select('h2[id]')] # get/return ksis
