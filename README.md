# Overview

Torn CLI is a tool to query the Torn API using the command line interface.

# Installation

Until I get around to properly structuring the repository as a python package,
it can be installed using the requirements.txt file. `torn` requires `click` and
`requests` packages.

```bash
pip install -r requirements.txt
```

# Usage

```bash
# I put the command on the $PATH. I suggest you do the same.

$ torn --help

# Requires an API key from torn to make requests.

$ apikey=<your api key>

$ torn $apikey user <field>

$ torn $apikey hospital

$ torn $apikey energy

$ torn $apikey nerve
```

I've been adding a programmable flag to these commands for bash scripts.

```bash
$ torn $apikey hospital --seconds

$ torn $apikey energy --delta

$ torn $apikey nerve --delta
```
