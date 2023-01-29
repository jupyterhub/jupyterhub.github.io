# JupyterHub Landing Page

This is a landing page for the JupyterHub Project.
Its goal is:

- To provide a high level overview of the project and its technical + social structure
- To point readers to other documentation and places to interact with the team

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
