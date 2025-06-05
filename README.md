ref: https://www.fedramp.gov/20x/standards/20x-ksi/


## Setup

Steps:

1. Create a virtual environment.
2. Activate the virtual environment in a subshell.
3. Install dependencies from `requirements.txt`.

Example:

```sh
# create svirtual environment
$ python3 -m venv ./ksis-venv

# start subshell
$ bash

# activate virtual environment
$ . ./ksis-env/bin/activate

# install dependencies
(ksis-venv) $ python3 -m pip install -r ./requirements.txt
```

## Usage

Steps:

1. Activate virtual environment.
2. Run `get.py` to parse [HTML][]-formatted KSIs into [JSON][].
3. Run `check.py` to validate `ksis.json` against [JSON schema][] in `./schema.json`.

Example:

```sh
# create subshell
$ bash

# activate virtual environment
$ . ksis-venv/bin/activate

# read KSIs as HTML from URL, write as JSON to ksis.json
$ ./get.py > ksis.json

# validate "ksis.json" against schema
$ ./check.py < ksis.json
```

[venv]: https://docs.python.org/3/library/venv.html
  "venv: Python virtual environment module"
[json]: "https:/json.org/"
  "JavaScript Object Notation"
[html]: https://en.wikipedia.org/wiki/HTML
  "HyperText Markup Language"
[json schema]: https://json-schema.org/
  "JSON schema"
