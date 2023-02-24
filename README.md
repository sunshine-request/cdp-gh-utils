# cdp-gh-utils

[![Build Status](https://github.com/CouncilDataProject/cdp-gh-utils/workflows/CI/badge.svg)](https://github.com/CouncilDataProject/cdp-gh-utils/actions)
[![Documentation](https://github.com/CouncilDataProject/cdp-gh-utils/workflows/Documentation/badge.svg)](https://CouncilDataProject.github.io/cdp-gh-utils)

Utility functions and scripts to manage CDP (and other) GitHub repositories.

---

## Installation

**Stable Release:** `pip install cdp-gh-utils`<br>
**Development Head:** `pip install git+https://github.com/CouncilDataProject/cdp-gh-utils.git`

## Running GitHub Actions from Command Line

⚠️ ⚠️ Note: make sure you have logged in to the [GitHub CLI](https://cli.github.com/)
with `gh auth login` prior to running any of these commands. ⚠️ ⚠️

### CLI

Run the `ci.yml` workflow from the `CouncilDataProject/cdp-gh-utils` repository.
(You can only run actions in repositories you have access to.)

```bash
run-gh-action CouncilDataProject/cdp-gh-utils ci.yml
```

With parameters:

```bash
run-gh-action CouncilDataProject/cdp-gh-utils ci.yml -k hello=world test=value
```

### Python

```python
from cdp_gh_utils import actions

result = actions.run(
    repo="CouncilDataProject/cdp-gh-utils",
    workflow_file_name="ci.yml",
    parameters={"hello": "world"},
)
```

## Documentation

For full package documentation please visit [CouncilDataProject.github.io/cdp-gh-utils](https://CouncilDataProject.github.io/cdp-gh-utils).

## Development

See [CONTRIBUTING.md](CONTRIBUTING.md) for information related to developing the code.

**MIT License**
