import feedparser
import yaml

def fetch_news():

    with open("feeds.yaml") as f:
        feeds = yaml.safe_load(f)

    articles = []

    for url in feeds["feeds"]:

        feed = feedparser.parse(url)

        for item in feed.entries:

            articles.append({

                "title": item.title,

                "url": item.link,

                "published":
                    item.get("published", ""),

                "source":
                    feed.feed.get("title", "")
            })

    return articles