"""
Build the site locally and preview it with an isolated environment.

* Use `-- live` to use a live webserver.
* Use `-- -r` to re-build the environment from scratch.
"""
import nox
from pathlib import Path

nox.options.reuse_existing_virtualenvs = True

build_command = ["-b", "dirhtml", "docs", "docs/_build/dirhtml"]


@nox.session
def docs(session):
    """Build the documentation. Use `-- live` for a live server to preview changes."""
    session.install("-r", "requirements.txt")
    if "live" in session.posargs:
        session.posargs.pop(session.posargs.index("live"))
        session.install("sphinx-autobuild")
        AUTOBUILD_IGNORE = [
            "_build",
        ]
        cmd = ["sphinx-autobuild"]
        # Autobuild requires absolute paths for some silly reason
        for folder in AUTOBUILD_IGNORE:
            folder = Path(folder).resolve()
            cmd.extend(f"--ignore {folder}".split())
    else:
        cmd = ["sphinx-build"]
    cmd.extend(build_command + session.posargs)
    session.run(*cmd)
