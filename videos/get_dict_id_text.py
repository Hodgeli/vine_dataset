# 读取final_texts.txt，生成字典dict_id_text
import re

f_id_texts = open("final_texts.txt", encoding='utf8', errors='ignore')


def get_text(template):
    rule = r'::::(.*?)\n'
    slot_list = re.findall(rule, template)
    return slot_list


def get_id(template):
    rule = r'(.*?)::::'
    slot_list = re.findall(rule, template)
    return slot_list


dict_id_text = {}
# for i in range(3):
while 1:
    line_id_text = f_id_texts.readline()
    if not line_id_text:
        break
    else:
        dict_id_text[str(get_id(line_id_text)[0])] = str(get_text(line_id_text)[0])


# print(dict_id_text['968589324889264128'])
f_id_texts.close()

f_id_texts = open("dict_id_text.txt", 'w', encoding='utf8', errors='ignore')
f_id_texts.write(str(dict_id_text))