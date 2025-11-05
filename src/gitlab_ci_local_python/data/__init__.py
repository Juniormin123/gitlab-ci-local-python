import json
from importlib import resources as importlib_resources


def get_npm_package_json() -> dict:
    with importlib_resources.as_file(importlib_resources.files("gitlab_ci_local_python.data") / "package.json") as j:
        return json.loads(j.read_text(encoding="utf-8"))
