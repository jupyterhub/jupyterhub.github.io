from subprocess import run
from pathlib import Path

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'JupyterHub Project'
copyright = '2023, JupyterHub Team'
author = 'JupyterHub Team'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["myst_parser", "jupyterhub_sphinx_theme"]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'jupyterhub_sphinx_theme'
html_title = "JupyterHub Project"
html_static_path = ['_static']
html_theme_options = {
    "external_links": [
      {"url": "https://jupyterhub-team-compass.readthedocs.io", "name": "🧭 Team Compass"},
      {"url": "https://discourse.jupyter.org/c/jupyterhub/10", "name": "💭 Community Forum"},
    ]
}

# -- Custom execution --------------------------------------------------------
script_blog_update = Path(__file__).parent / "scripts" / "download_jupyterhub_feed.py"
run(f"python {script_blog_update}", shell=True)
