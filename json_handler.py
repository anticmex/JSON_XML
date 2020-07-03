from function_storage import *
import json

word_mentions = {}

with open("newsafr.json", encoding="utf-8") as f:
    json = json.load(f)
    for len_news in range(len(json['rss']['channel']['items'])):
        for word in (json['rss']['channel']['items'][len_news]['description'].split(" ")):
            get_sorted_set(word, word_mentions)

    top_set = sorted(set(list(word_mentions.values())), reverse=True)

watch_result(word_mentions, top_set)
