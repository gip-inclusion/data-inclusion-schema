# AGENTS.md

## Stack

- type-hinted python
- uv based project
- pydantic
- pytest

## Convention

- language:
    - french for docs, github, git, code (domain models, etc.)
    - english for internal code

## Commands

- run tests with `uv run --group test pytest`
- build docs with `uv run --group docs scripts/compile_docs.py`
- build json schema with `uv run scripts/compile_schema.py`

## Rules

- keep the `CHANGELOG.md` updated
- keep the schema artifacts updated
