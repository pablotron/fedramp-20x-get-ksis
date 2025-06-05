# fedramp-20x-get-ksis

Scraper and validator for [FedRAMP][] [Key Security Indicators
(KSIs)][ksis].

## Setup

Steps:

1. Create a virtual environment.
2. Activate the virtual environment in a subshell.
3. Install dependencies from `requirements.txt` with [pip][].

Example:

```sh
# create svirtual environment
$ python3 -m venv ./ksis-venv

# start subshell
$ bash

# activate virtual environment
$ . ./ksis-env/bin/activate

# install dependencies with pip
(ksis-venv) $ python3 -m pip install -r ./requirements.txt
```

**Note:** In [Debian][] and [Ubuntu][] you may also need to install the
`python3-pip` and `python3-venv` packages, like this:

```sh
# install python3-pip and python3-venv packages
sudo apt install python3-pip python3-venv
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

# read KSIs as HTML from URL, write as JSON to "ksis.json"
$ ./get.py > ksis.json

# validate "ksis.json" against schema
$ ./check.py < ksis.json
```

[venv]: https://docs.python.org/3/library/venv.html
  "venv: Python virtual environment module"
[pip]: https://pypi.org/project/pip/
  "pip: Python package installer"
[json]: "https:/json.org/"
  "JavaScript Object Notation"
[html]: https://en.wikipedia.org/wiki/HTML
  "HyperText Markup Language"
[json schema]: https://json-schema.org/
  "JSON schema"
[fedramp]: https://www.fedramp.gov/
  "FedRAMP"
[ksis]: https://www.fedramp.gov/20x/standards/20x-ksi/
  "FedRAMP 20x Key Security Indicators (KSIs)."
[debian]: https://www.debian.org/
  "Debian Linux"
[ubuntu]: https://ubuntu.com/
  "Ubuntu Linux"
