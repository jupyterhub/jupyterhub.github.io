"""
Build the site locally and preview it with an isolated environment.

* Use `-r` to re-build the environment from scratch.
"""

from pathlib import Path

import nox

nox.options.reuse_existing_virtualenvs = True


def _fetch_data(session):
    session.install("-r", "requirements.txt")
    session.run("python", "docs/scripts/download_jupyterhub_feed.py")
    # Cache the downloaded file so we don't re-download on local builds
    # Deleting this file will force a re-download.
    if not Path("docs/_data/repositories.json").exists():
        session.run("python", "docs/scripts/download_repositories.py")


@nox.session
def docs(session):
    """Build the documentation as static HTML."""
    _fetch_data(session)
    session.chdir("docs")
    session.run("myst", "build", "--html", *session.posargs)


@nox.session(name="docs-live")
def docs_live(session):
    """Start a live-preview server for the documentation."""
    _fetch_data(session)
    session.chdir("docs")
    session.run("myst", "start", *session.posargs)
