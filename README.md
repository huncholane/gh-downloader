# GitHub Folder Downloader

## Overview

`gh-downloader` is a command-line tool that allows you to download a specific folder or an entire repository from GitHub without cloning the full repository history.

## Installation

To install the tool, use the following command:

```bash
pip install .
```

Alternatively, you can install it directly from GitHub:

```bash
pip install git+https://github.com/huncholane/gh-downloader.git
```

## Usage

To download a folder or an entire repository, use:

```bash
gh-downloader <GitHub_URL>
```

### Examples

#### Download an entire repository:

```bash
gh-downloader https://github.com/user/repo
```

#### Download a specific folder from a repository:

```bash
gh-downloader https://github.com/user/repo/tree/main/folder_name
```

## Features

- Downloads only the required folder or the whole repository.
- Uses a temporary directory to clone before extracting.
- Removes the `.git` directory after cloning to keep it clean.
- Supports merging into an existing folder.

## Dependencies

- Python 3.x
- `requests`

## Contributing

Feel free to submit issues or pull requests to improve `gh-downloader`.

## License

This project is licensed under the MIT License.
