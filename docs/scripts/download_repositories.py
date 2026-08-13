"""Download the list of active repositories in the jupyterhub org for the myst-listing plugin.

We use the plain GitHub API instead of the `gh` CLI because it works without authentication
and ReadTheDocs builders don't have `gh` installed.
If we start hitting rate limits, we should give GH_TOKEN to ReadTheDocs
"""
import json
import os
from pathlib import Path
from urllib.request import Request, urlopen

# One page of 100 covers the org's ~76 repos; add pagination if it ever outgrows that.
url = "https://api.github.com/orgs/jupyterhub/repos?per_page=100"
token = os.environ.get("GH_TOKEN")
headers = {"Authorization": f"Bearer {token}"} if token else {}
repos = json.load(urlopen(Request(url, headers=headers)))

records = [
    {
        "title": repo["name"],
        "url": repo["html_url"],
        "description": repo["description"],
        "stars": repo["stargazers_count"],
        "updated": repo["updated_at"][:10],
    }
    for repo in repos
    if not repo["archived"]
]

path_out = Path(__file__).parent.parent / "_data" / "repositories.json"
path_out.write_text(json.dumps(records, indent=1))
print(f"Wrote {len(records)} repositories to\n{path_out}")
