import json

word_mentions = {}

with open("newsafr.json", encoding="utf-8") as f:
    json = json.load(f)
    for len_news in range(len(json['rss']['channel']['items'])):
        for word in (json['rss']['channel']['items'][len_news]['description'].split(" ")):
            if len(word) > 6:
                if word in word_mentions:
                    word_mentions[word] += 1
                else:
                    word_mentions[word] = 1
    top_set = sorted(set(list(word_mentions.values())), reverse=True)

    counter = 0
    for n, i in enumerate(top_set):
        for key, val in word_mentions.items():
            if i == val and counter < 10:
                print(f'Слово "{key}" встречается в тексте - {i} раз.')
                counter += 1
