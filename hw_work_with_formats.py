from pprint import pprint
import json

def get_words_in_description():
    list_of_des = []
    for f in item:
        for k, values in f.items():
            if k == 'description':
                words_in_description = values.split()
                list_of_des.append(words_in_description)
    return list_of_des

def top10():
    words_dict = {}
    for w in get_words_in_description():
        for word in w:
            #pprint(word)
            if len(word) > 6:
                word6 = word
                if word6 in words_dict:
                    words_dict[word6] += 1
                else:
                    words_dict[word6] = 0
    list = []
    for i in words_dict:
        k = (i, words_dict[i])
        list.append(k)
    sorlist = sorted(list, key=lambda s: s[1], reverse=True)
    sorlist = sorlist[0:10]
    print('топ 10 самых часто встречающихся в новостях слов длиннее 6 символов:')
    for i in sorlist:
        print(f'слово "{i[0]}" - {i[1]} раз')
    return words_dict

with open('newsafr.json', encoding='utf8') as datafile:
    json_data = json.load(datafile)
    item = json_data['rss']['channel']['items']
    top10()


import xml.etree.ElementTree as ET
tree = ET.parse("newsafr.xml")
root = tree.getroot()
xml_description = root.findall("channel/item/description")

#print(root.tag)
#print(root.attrib)
#xml_title = root.find("channel/title")
#print(xml_title.text)
#xml_items = root.findall("channel/item")
#print(len(xml_items))
#for xmli in xml_items:
    #print(xmli.attrib["id"])

def get_words_in_description_xml():
    list_of_des = []
    for description in xml_description:
        list = [description.text]
        for l in list:
            words_in_description = l.split()
            list_of_des.append(words_in_description)
    return list_of_des

def top10_xml():
    words_dict = {}
    for w in get_words_in_description_xml():
        for word in w:
            #pprint(word)
            if len(word) > 6:
                word6 = word
                if word6 in words_dict:
                    words_dict[word6] += 1
                else:
                    words_dict[word6] = 0
    list = []
    for i in words_dict:
        k = (i, words_dict[i])
        list.append(k)
    sorlist = sorted(list, key=lambda s: s[1], reverse=True)
    sorlist = sorlist[0:10]
    print('топ 10 самых часто встречающихся в новостях слов длиннее 6 символов:')
    for i in sorlist:
        print(f'слово "{i[0]}" - {i[1]} раз')
    return words_dict

top10_xml()