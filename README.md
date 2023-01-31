# JupyterHub Landing Page

This is a landing page for the JupyterHub Project.
It is accessible at [**`hub.jupyter.org`**](https://hub.jupyter.org).

## Goals

Its goal is:

- To provide a high level overview of the project and its technical + social structure
- To point readers to other documentation and places to interact with the team

## Implementation

This is a GitHub Pages site that is being built with the action in `.github/workflows`.
We added a `CNAME` to the `jupyter.org` DNS entries [following these github instructions](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site).

It is built with Sphinx and the [JupyterHub Sphinx Theme](https://github.com/jupyterhub/jupyterhub-sphinx-theme).

## To build the site with `nox`

Follow these steps:

1. **Install `nox`**:

   ```shell
   pip install nox
   ```
2. **Build the site with `nox`**:

   ```shell
   nox -s docs
   ```

   Or with a server that lets you preview pages and auto-update with changes:

   ```shell
   nox -s docs -- live
   ```

## To build the site locally

1. **Install dependencies**:

   ```shell
   pip install -r requirements.txt
   ```
2. **Build with Sphinx**:

   ```shell
   sphinx-build docs docs/_build/dirhtml -b dirhtml
   ```
