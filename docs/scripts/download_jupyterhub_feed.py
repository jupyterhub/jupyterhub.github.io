import feedparser
from pathlib import Path

URL_JUPYTER_BLOG = "https://medium.com/feed/jupyter-blog/tagged/jupyterhub"
d = feedparser.parse(URL_JUPYTER_BLOG)

md = []
for entry in d.entries[:10]:
    md.append(f"- [{entry.title}]({entry.link}) by **{entry.author}**")

path_out = Path(__file__).parent.parent / "_data" / "blog-posts.txt"
path_out.write_text("\n".join(md))

print(f"Finished writing links to latest blog posts in\n{path_out}...")
