# Overview

Torn CLI is a tool to query the Torn API using the command line interface.

# Installation

Until I get around to properly structuring the repository as a python package,
it can be installed using the requirements.txt file. `torn` requires `click` and
`requests` packages.

```bash
pip install -r requirements.txt

# I put the commands in my bin which is on $PATH. I suggest you do the same.
ln $HOME/bin/torn $(PWD)/cli-torn.py
ln $HOME/bin/torn-api $(PWD)/cli-api.py
```

# Usage

```bash
# Requires an API key from torn to make requests.
$ apikey=<your api key>
```

```bash
$ torn --help

$ torn $apikey hospital

$ torn $apikey energy

$ torn $apikey nerve

$ torn $apikey property-time
```

```bash
$ torn-api --help

$ torn-api $apikey user <field>

$ torn-api $apikey property <field>
```

I've been adding a programmable flags to these commands for bash scripts.

```bash
$ torn $apikey hospital --seconds

$ torn $apikey energy --delta

$ torn $apikey nerve --delta
```
