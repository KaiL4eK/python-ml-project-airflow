# Project README! Here we go!

<div align="center">

[![PythonSupported](https://img.shields.io/badge/python-3.9-brightgreen.svg)](https://python3statement.org/#sections50-why)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://pre-commit.com/)

Awesome `python-ml-project-airflow` project!

</div>

- [Repository contents](#repository-contents)
- [System requirements](#system-requirements)
- [How to run/debug code](#how-to-rundebug-code)
- [Other interesting info](#other-interesting-info)

## Repository contents

- [docs](docs) - documentation of the project
- [reports](reports) - reports generated (as generated from notebooks)
  > Check if you need to ignore large reports or keep them in Git LFS
- [configs](configs) - configuration files directory

- [notebooks](notebooks) - directory for `jupyter` notebooks
- [tests](tests) - project tasts based on [pytest](https://docs.pytest.org/en/stable/)
- [scripts](scripts) - repository service scripts
  > These ones are not included into the pakckage if you build one - these scripts are only for usage with repository
- [python_ml_project_airflow](python_ml_project_airflow) - source files of the project
- [.editorconfig](.editorconfig) - configuration for [editorconfig](https://editorconfig.org/)

- [.gitignore](.gitignore) - the files/folders `git` should ignore
- [.pre-commit-config.yaml](.pre-commit-config.yaml) - [pre-commit](https://pre-commit.com/) configuration file
- [README.md](README.md) - the one you read =)
- [DEVELOPMENT.md](DEVELOPMENT.md) - guide for development team
- [Makefile](Makefile) - targets for `make` command
- [cookiecutter-config-file.yml](cookiecutter-config-file.yml) - cookiecutter project config log
- [poetry.toml](poetry.toml) - poetry local config
- [pyproject.toml](pyproject.toml) - Python project configuration
- [requirements.project.txt](requirements.project.txt) - Python project requirements (e.g. poetry and may be other packages to be installed before installing core packages)

## System requirements

- Python version: 3.9
- Operating system: Ubuntu or WSL
- Poetry version >= 1.8.0

> We tested on this setup - you can try other versions or operation systems by yourself!

## How to run/debug code

You can run code using instructions from [docs/Dev-Debug.md](docs/Dev-Debug.md).

## Other interesting info

Here you can write anything about your project!
