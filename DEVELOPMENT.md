# Development guide

This is guide how to prepare development environment and use main tools

## Table of contents

- [Development guide](#development-guide)
  - [Table of contents](#table-of-contents)
  - [Prerequisites](#prerequisites)
  - [Initialize your code](#initialize-your-code)
    - [Just created project?](#just-created-project)
    - [Cloned existing project](#cloned-existing-project)
  - [Optional setup steps](#optional-setup-steps)
  - [Some known issues](#some-known-issues)

## Prerequisites

> If you need to install tools, check links

- [Python](docs/TOOLS.md#python)
- [Poetry](docs/TOOLS.md#poetry)
- [Make](docs/TOOLS.md#make)

## Initialize your code

### Just created project?

0. Create repository on your favourite server (Bitbucket, Github or other) and obtain "Version control system URL" like this one:

```url
https://github.com/user/my-project.git
```

1. Create folder and initialize `git` inside your repo folder:

```bash
cd python-ml-project-airflow && git init
```

2. Initialize poetry and install `pre-commit` hooks:

```bash
make project-init
```

3. Upload initial code to GitHub:

```bash
git add .
git commit -m ":tada: Initial commit"
git branch -M develop
git remote add origin <Version control system URL>
git push -u origin develop
```

[Table of contents](#table-of-contents)

### Cloned existing project

1. Initialize poetry and install `pre-commit` hooks:

```bash
make project-init
```

[Table of contents](#table-of-contents)

## Optional setup steps

1. Install VSCode Extensions
   - [EditorConfig for VS Code](https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig)
      Open control panel (Ctrl+P) and enter `ext install EditorConfig.EditorConfig`

1. To initialize generation of Table of Contents from notebook headers we use `nbextension`:

    - `nbextention-toc-install`

    > It is required version nbconvert~=5.6.1 (checked for date 2021-12-29)

    - To export notebook with ToC use next command:

      ```bash
      poetry run jupyter nbconvert --template toc2 --to html_toc --output-dir ./exports <путь до файла>
      ```

      > For example, `poetry run jupyter nbconvert --template toc2 --to html_toc --output-dir ./exports notebooks/example.ipynb`

      To use embedded images into HTML use option `html_embed`:

      ```bash
      poetry run jupyter nbconvert --template toc2 --to html_embed --output-dir ./exports <путь до файла>
      ```

[Table of contents](#table-of-contents)

## Some known issues

- If you have issues with python version like:

    ```bash
    The currently activated Python version 3.9.7 is not supported by the project (~3.9.0)
    ...
    NoCompatiblePythonVersionFound
    ...
    ```

    Check version of your `python3` binary and make sure you have python3.9 installed.

[Table of contents](#table-of-contents)
