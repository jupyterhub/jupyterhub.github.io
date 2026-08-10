import feedparser
import yaml
from pathlib import Path
from time import strftime

# A list of all blog posts with the "jupyterhub" tag
URL_JUPYTER_BLOG = "https://medium.com/feed/jupyter-blog/tagged/jupyterhub"

if __name__ == "__main__":
    resp = feedparser.parse(URL_JUPYTER_BLOG)
    # Rearrange so that we can write to YAML for the listing plugin
    records = [
        {
            "title": entry.title,
            "url": entry.link,
            "author": entry.author,
            "date": strftime("%Y-%m-%d", entry.published_parsed),
        }
        for entry in resp.entries
    ]

    path_out = Path(__file__).parent.parent / "_data" / "blog-posts.yml"
    path_out.write_text(yaml.safe_dump(records, sort_keys=False))

    print(f"Finished writing links to latest blog posts in\n{path_out}...")
