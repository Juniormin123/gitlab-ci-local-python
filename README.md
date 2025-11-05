# gitlab-ci-local-python

[![PyPI version](https://badge.fury.io/py/gitlab-ci-local-python.svg)](https://badge.fury.io/py/gitlab-ci-local-python)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Python wrapper for [gitlab-ci-local](https://github.com/firecow/gitlab-ci-local).

## Requirements

- Python 3.10 or higher
- `uv` for development

## Installation

```bash
pip install gitlab-ci-local-python
```

Or using `uv`:

```bash
uv pip install gitlab-ci-local-python
```

## Usage

### Basic Usage

Run your GitLab CI pipeline locally:

```bash
gitlab-ci-local-python
```

Or use the shorter alias:

```bash
gcl-py
```

### Pass Arguments

All arguments are passed directly to `gitlab-ci-local`:

```bash
# Run a specific job
gitlab-ci-local-python build

# List all jobs
gitlab-ci-local-python --list

# Run with specific variables
gitlab-ci-local-python --variable FOO=bar

# Preview mode
gitlab-ci-local-python --preview
```

### Show Version Information

Display the Node.js and npm versions being used:

```bash
gitlab-ci-local-python show-meta-info
```

## How It Works

1. **Automatic Installation**: On first run, the package automatically installs `gitlab-ci-local` (v4.63.0+) via npm to `~/.local/cache/gitlab-ci-local-python/gitlab-ci-local`
2. **Bundled Node.js**: Uses [nodejs-wheel](https://pypi.org/project/nodejs-wheel/) to provide a Python-bundled Node.js runtime
3. **Pass-through Execution**: All CLI arguments are forwarded to the underlying `gitlab-ci-local` command

## Environment Variables

- `GCL_PY_FORCE_REINSTALL`: Set to `1` to force reinstallation of the npm package on each run
  ```bash
  GCL_PY_FORCE_REINSTALL=1 gitlab-ci-local-python
  ```

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Credits

- Built on top of [gitlab-ci-local](https://github.com/firecow/gitlab-ci-local) by firecow
- Uses [nodejs-wheel](https://pypi.org/project/nodejs-wheel/) for Python-bundled Node.js
