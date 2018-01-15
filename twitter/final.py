import os
import re


def file_name(file_dir):  # 获取视频名list
    for root, dirs, files in os.walk(file_dir):
        continue
    return files


def get_id(template):
    rule = r'(.*?)::::'
    slot_list = re.findall(rule, template)
    return slot_list


def get_text(template):
    rule = r'::::(.*?)\n'
    slot_list = re.findall(rule, template)
    return slot_list


f_id_text = open("id_text_final.txt", encoding='utf8', errors='ignore')
dict_id_text = {}
while 1:
    line_text = f_id_text.readline()
    if not line_text:
        break
    else:
        dict_id_text[get_id(line_text)[0]] = get_text(line_text)[0]
print('dict_id_text生成成功：' + str(len(dict_id_text)))

list_final_txt = file_name('./hash_twitter_new')
print(len(list_final_txt))

i = 0
for hash in list_final_txt:
    f_hash = open("./hash_twitter_new/" + hash, encoding='utf8', errors='ignore')
    long_str = f_hash.readline()
    f_hash.close()
    list_word = long_str.split(' ')
    if(len(list_word) < 10):
        # while (len(list_word) < 12):
        #
        #     list_pop = dict_id_text.popitem()
        #     long_str += list_pop[1]
        #     list_word = long_str.split(' ')
        # print(long_str)
        # i += 1
        # f_hash = open("./hash_twitter_new/" + hash, 'w', encoding='utf8', errors='ignore')
        # f_hash.write(str(long_str))
        # f_hash.close()
        print(hash)
print(i)
