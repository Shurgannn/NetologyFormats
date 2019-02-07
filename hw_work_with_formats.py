from pprint import pprint
import json

def get_words_in_description():
    for f in item:
        for k, values in f.items():
            if k == 'description':
                words_in_description = values.split()
                print(words_in_description)
    return words_in_description

def top10():
    for word in words_in_description:
        if len(word) > 6:
            word6 = word.strip()
        if word6 in words_dict:
            words_dict[word6] += 1
        else:
            words_dict[word6] = 0
        print(words_dict)
        words_dict = sorted(words_dict.items())
        print(words_dict)
    return words_dict

with open('newsafr.json', encoding='utf8') as datafile:
    json_data = json.load(datafile)
    item = json_data['rss']['channel']['items']
    #get_words_in_description()
    #words_dict = {}
    #top10()


import xml.etree.ElementTree as ET
tree = ET.parse("newsafr.xml")
root = tree.getroot()
#print(root.tag)
#print(root.attrib)
#xml_title = root.find("channel/title")
#print(xml_title.text)
#xml_items = root.findall("channel/item")
#print(len(xml_items))
#for xmli in xml_items:
    #print(xmli.attrib["id"])


xml_description = root.findall("description/description")
print(xml_description)
for description in xml_description:
    print(description.attrib)
