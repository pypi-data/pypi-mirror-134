[![Build](https://img.shields.io/github/workflow/status/cbuschka/installed-packages-diff/build)](https://github.io/cbuschka/installed-packages-diff) [![PyPI](https://img.shields.io/pypi/v/installed-packages-diff)](https://pypi.org/project/installed-packages-diff/) [![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)](https://github.com/cbuschka/installed-packages-diff/blob/main/license.txt)
# installed-packages-diff - Compare packages and versions on servers

## Features

* collects packages and version via ssh
* calculated and prints the differences
* supports rpm and dpkg

## Prerequisites

* GNU make
* python >= 3.6
* virtualenv

## Usage

Create a config as described below.

```bash
pip install --user installed-packages-diff

python3 -m installed_packages_diff ./config.yaml
```

## Development

### Setup

```bash
make install_deps
```

### Run tests

```bash
make tests
```

### Create a config config.yml

```yaml
version: 'installed-packages-diff/3'
groups:
  web:
    type: rpm # or dpkg
    servers:
      - url: ssh://root@web-dev
        excludes:
          - "missing"
      - url: ssh://root@web-live
```

### Run installed-packages-diff

```bash
make run
```

## License

Copyright (c) 2021 by [Cornelius Buschka](https://github.com/cbuschka).

[MIT](./license.txt)
