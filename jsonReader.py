import json
from pprint import pprint

data = json.load(open('reddit_news_json.json'))
for article in data:
    pprint(article['title']), "\n"