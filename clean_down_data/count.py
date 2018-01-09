# 统计hash总数与词频
import collections
import re


def get_id(template):
    rule = r'(.*?)::::'
    slot_list = re.findall(rule, template)
    return slot_list


def get_text(template):
    rule = r'::::(.*?)\n'
    slot_list = re.findall(rule, template)
    return slot_list


def get_list_or_dict(path):
    f = open(path, encoding='utf8', errors='ignore')
    a = f.read()
    dict_or_list = eval(a)
    f.close()
    return dict_or_list


list_id = get_list_or_dict('list_id.txt')
print('list_id长度' + str(len(list_id)))

f_id_hash_final = open("id_hash_final.txt", 'w', encoding='utf8', errors='ignore')

f = open("final_hashs.txt", encoding='utf8', errors='ignore')
dict_id_hash = {}
while 1:
    line_txt = f.readline()
    if not line_txt:
        break
    else:
        dict_id_hash[get_id(line_txt)[0]] = get_text(line_txt)[0]
f.close()
print('dict_id_hash长度' + str(len(dict_id_hash)))  # 121117
f_dict_id_hash = open("dict_id_hash.txt", 'w', encoding='utf8', errors='ignore')
f_dict_id_hash.write(str(dict_id_hash))
f_dict_id_hash.close()

for id in list_id:
    id = id.replace('.mp4', '')

    f_id_hash_final.write(id + '::::' + dict_id_hash[id] + '\n')
f_id_hash_final.close()

f_id_hash_final = open("id_hash_final.txt", encoding='utf8', errors='ignore')
f_count_hash = open("count_hash.txt", 'w', encoding='utf8', errors='ignore')


def subString1(template):  # HashTag以‘#’开头，以空格或回车结尾
    copy = False
    finished = False
    slotList = []
    str = ""
    for s in template:
        if s == '#':
            copy = True
        elif s == ' ':
            copy = False
            finished = True
        elif s == '\n':
            copy = False
            finished = True
        elif copy:
            str = str + s
        if finished:
            if str != "":
                slotList.append(str)
            str = ""
            finished = False
    return slotList


slotList = []
i = 1
# for i in range(0,3):
while 1:
    line_id_hash = f_id_hash_final.readline()
    if not line_id_hash:
        break
    else:
        # print()
        slotList += subString1(line_id_hash)  # 将所有HashTag存进list
# print(slotList)

result = collections.Counter(slotList)  # 词频统计
# ss = str(result)    #词频统计结果转换成字符串并存文件
# f_handle_hash.write(ss)
# print(result.most_common(100)) 查看统计结果前100名
for each in result.most_common():
    ss = str(each)  # 词频统计结果转换成字符串并存文件
    f_count_hash.write(ss + '\n')
    # print(ss)
f_id_hash_final.close()
f_count_hash.close()
