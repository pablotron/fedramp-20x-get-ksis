# fedramp-20x-get-ksis

[Python][] scripts for working with [FedRAMP 20x Key Security Indicators
(KSIs)][ksis].

Scripts in this repository:

- `check.py`: Check [JSON][] emitted by `get.py` against [JSON schema][] in `schema.json`.
- `get.py`: Fetch [HTML][] from the [FedRAMP 20x KSIs site][ksis], extract the KSIs, and print them to standard output as [JSON][].
- `ksis-csv.py`: Read [JSON][] of KSIs from standard input and write a [CSV][] of KSIs to standard output.

Other files:

- `ksis.json`: [JSON][] of KSIs from the [FedRAMP 20x KSIs site][ksis] as of 2025-06-05.
- `requirements.txt`: [Pip][]-friendly dependencies.
- `schema.json`: [JSON schema][] used by `check.py` to validate [JSON][] emitted by `get.py`.

See the [Usage section](#usage "Usage") below for additional
documentation.

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
3. Run `ksis-csv.py` to generate a [CSV][] of KSIs.

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

# generate a CSV of KSIs as "ksis.csv"
$ ./ksis-csv.py < ksis.json > ksis.csv
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
[csv]: https://en.wikipedia.org/wiki/Comma-separated_values
  "Comma-separated values (CSV)"
[python]: https://python.org/
  "Python programming language"
