# Adversary Emulation Planner Web Frontend

This tool can be used to automatically build an ordered set of attack stages
with [MITRE ATT&CK](https://attack.mitre.org/) techniques executed during each stage.

The output is a set of attack stages that show all possible techniques that an
adversary might execute during each stage.

## Installation

Install using pip:

```bash
pip install aep-web
```
You will also need to clone the [aep-data](https://github.com/mnemonic-no/aep-data) repository, which contains a starting point witch example data:

```bash
git clone https://github.com/mnemonic-no/aep-data
```

## Run
```bash
git clone https://github.com/mnemonic-no/aep-data
aep-web --port <PORT> --data-dir /path/to/aep/data-dir
```

### Options

Available options

```
--reload            Watch for file changes and reload webserver upon change
                    (Useful for development)
--web-reoot <PATH>  Need if running behind a reverse proxy with another path than /
--data-dir <PATAH>  Path to aep-data directory
--port <PORT>       Listen on PORT (default is 3000)
--host <HOST>       Host intefrace to listen to (default is 127.0.0.1)
```
