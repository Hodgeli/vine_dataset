import re
import os


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


###########生成list_short_hash.txt

# f_hash = open("count_hash.txt", encoding='utf8', errors='ignore')
# list_hash = []
# while 1:
#     line_hash = f_hash.readline()
#     if not line_hash:
#         break
#     else:
#         list_hash.append(str(re.findall(r"'(.*?)'", line_hash, flags=0)[0]))
# print('list_hash生成成功：' + str(len(list_hash)))
#
# list_hash_ok = file_name(r'./hash_twitter_new')
# print('list_hash_ok生成成功：' + str(len(list_hash_ok)))
#
# list_short_hash = []
# for hash in list_hash:
#     if hash not in list_hash_ok:
#         list_short_hash.append(hash)
#
# f_list_short_hash = open("list_short_hash.txt", 'w', encoding='utf8', errors='ignore')
# f_list_short_hash.write(str(list_short_hash))
# f_list_short_hash.close()

list_final_txt = file_name('./hash_twitter_new')
print(len(list_final_txt))

list_short_hash = []
for hash in list_final_txt:
    f_hash = open("./hash_twitter_new/" + hash, encoding='utf8', errors='ignore')
    long_str = f_hash.readline()
    list_word = long_str.split(' ')
    if (len(list_word) < 10):
        list_short_hash.append(hash)
    f_hash.close()
print('list_short_hash生成成功：' + str(len(list_short_hash)))

f_id_hash = open("final_hashs.txt", encoding='utf8', errors='ignore')
dict_id_hash = {}
while 1:
    line_text = f_id_hash.readline()
    if not line_text:
        break
    else:
        dict_id_hash[get_id(line_text)[0]] = get_text(line_text)[0]
print('dict_id_hash生成成功：' + str(len(dict_id_hash)))

f_id_text = open("id_text_final.txt", encoding='utf8', errors='ignore')
dict_id_text = {}
while 1:
    line_text = f_id_text.readline()
    if not line_text:
        break
    else:
        dict_id_text[get_id(line_text)[0]] = get_text(line_text)[0]
print('dict_id_text生成成功：' + str(len(dict_id_text)))

print('-------开始生成--------')
i = 0
for hash in list_short_hash:
    long_str = ''
    for id in dict_id_hash:
        if str(hash) in str(dict_id_hash[id]):
            long_str += str(dict_id_text[id])
    f_twitter_new = open('./hash_twitter_new/' + hash, 'w', encoding='utf8', errors='ignore')
    f_twitter_new.write(long_str)
    f_twitter_new.close()
    i += 1
    if(i % 100 == 0):
        print(i)
print('生成结束')