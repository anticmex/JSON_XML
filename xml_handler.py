#обработчик xml файлов

import xml.etree.cElementTree as ET
parser = ET.XMLParser(encoding = "utf-8")
tree = ET.parse('newsafr.xml', parser)
root = tree.getroot()

word_mentions = {}
def line_description(line):
    return line.find("description").text.split(" ")


for xml in root.findall("channel/item"):
    for word in line_description(xml):
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