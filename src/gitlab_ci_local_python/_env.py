import os
from typing import Final


GCL_PY_FORCE_REINSTALL: Final[bool] = os.getenv("GCL_PY_FORCE_REINSTALL", "0") == "1"
"""Set this environment variable to "1" to force reinstallation of `gitlab-ci-local` npm package on each run."""
