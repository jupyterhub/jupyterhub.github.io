#!/usr/bin/env bash
# This just lists out a `gh` script so that it's easier to read/re-use than putting it all in noxfile.py
# It downloads the list of active repositories in the jupyterhub org for the myst-listing plugin to use.
# Make sure to run it from the same folder because the output path is relative to this script.
gh repo list jupyterhub --limit 200 --no-archived \
  --json name,url,description,stargazerCount,updatedAt \
  --jq '[.[] | {title: .name, url, description, stars: .stargazerCount, updated: .updatedAt[:10]}]' \
  > "$(dirname "$0")/../_data/repositories.json"
