#обработчик xml файлов

from function_storage import *
import xml.etree.cElementTree as ET
parser = ET.XMLParser(encoding = "utf-8")
tree = ET.parse('newsafr.xml', parser)
root = tree.getroot()

word_mentions = {}

for xml in root.findall("channel/item"):
    for word in line_description(xml):
        get_sorted_set(word, word_mentions)

top_set = sorted(set(list(word_mentions.values())), reverse=True)

watch_result(word_mentions, top_set)
