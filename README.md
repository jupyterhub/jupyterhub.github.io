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

It is built with [mystmd](https://mystmd.org/).

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
   nox -s docs-live
   ```

## To build the site locally

1. **Install dependencies**:

   ```shell
   pip install -r requirements.txt
   ```
2. **Build with mystmd**:

   ```shell
   cd docs && myst build --html
   ```

## Web hosting

### GitHub Pages for the live site

This site is hosted with GitHub Pages, so that all of the other repositories in `jupyterhub/` that use GitHub Pages will automatically be served at `hub.jupyter.org/[repository]`.

### ReadTheDocs for PR Previews

We use ReadTheDocs just for PR previews.
If you'd like access to the ReadTheDocs site, ask a team member.
The `main` branch is "hidden" in the RTD configuration so it won't show up in web searches, since we use GitHub Pages for the live site.
