# Contributing

## Local prerequisites

### `python`

Project uses `python3.10`

[`pyenv`](https://github.com/pyenv/pyenv) is a clean and easy way to manage multiple python versions on your computer. Installation instructions are available [here](https://github.com/pyenv/pyenv-installer).

## Setup

```bash
# Clone this repository
git clone git@github.com:betagouv/data-inclusion-schema.git

# Create a new virtualenv in the project's root directory
python3.10 -m venv .venv --prompt di-schema

# Activate the environment
source .venv/bin/activate
pip install -U pip setuptools wheel

# Install package in editable mode and dependencies
pip install -e .[dev]

# Setup code quality tools
pre-commit install
```

## Generating the json schemas

```bash
data-inclusion-schema structure > structures.json
data-inclusion-schema service > services.json
```