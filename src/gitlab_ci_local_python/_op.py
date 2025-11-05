import json
import sys
from pathlib import Path
from typing import Final, TypeAlias, cast

from nodejs_wheel import npm

from gitlab_ci_local_python._env import GCL_PY_FORCE_REINSTALL
from gitlab_ci_local_python.data import get_npm_package_json

NodeVer: TypeAlias = str
NpmVer: TypeAlias = str


DEFAULT_NPM_CWD: Final[Path] = Path.home() / ".local" / "cache" / "gitlab-ci-local-python" / "gitlab-ci-local"


def get_node_npm_version() -> tuple[NodeVer, NpmVer]:
    """Return the installed Node.js and npm versions as a tuple."""
    node_proc = npm(
        ["--version"],
        return_completed_process=True,
        text=True,
        check=True,
        capture_output=True,
    )
    node_version = cast(str, node_proc.stdout.strip())  # text=True ensures stdout is str

    npm_proc = npm(
        ["--version"],
        return_completed_process=True,
        text=True,
        check=True,
        capture_output=True,
    )
    npm_version = cast(str, npm_proc.stdout.strip())  # text=True ensures stdout is str
    return node_version, npm_version


def init_gitlab_ci_local(force_reinstall: bool = GCL_PY_FORCE_REINSTALL) -> Path:
    """Install `gitlab-ci-local` npm package locally and return its path.

    The package will be installed to `~/.local/cache/gitlab-ci-local-python/gitlab-ci-local`.
    """
    (np := DEFAULT_NPM_CWD).mkdir(parents=True, exist_ok=True)
    j = get_npm_package_json()
    with open(np / "package.json", "w", encoding="utf-8") as f:
        json.dump(j, f, indent=2)
    # check existence
    if (
        npm(
            [
                "ls",
                "gitlab-ci-local",
            ],
            cwd=np,
            capture_output=True,
        )
        == 0
        and not force_reinstall
    ):
        return np
    else:
        print(f"Installing gitlab-ci-local npm package to {np!s}", file=sys.stderr)
        npm(
            [
                "install",
                "gitlab-ci-local",
                "--no-save",
                "--no-audit",
                "--no-fund",
            ],
            cwd=np,
            check=True,
        )
        return np


def run_gitlab_ci_local(args: list[str]) -> int:
    """Run `gitlab-ci-local` with the given arguments.

    :return: The return code of the `gitlab-ci-local` process.
    """
    np = init_gitlab_ci_local()
    return npm(
        ["start", "--"] + args,
        cwd=np,
    )
