import re


def getText(template):
    rule = r'::::(.*?)\n'
    slotList = re.findall(rule, template)
    return slotList


def get_list_or_dict(path):
    f = open(path, encoding='utf8', errors='ignore')
    a = f.read()
    dict_or_list = eval(a)
    f.close()
    return dict_or_list


f_count_hash = open("count_hash.txt", encoding='utf8', errors='ignore')
# f_list_count_hash = open("list_count_hash.txt",'w',encoding='utf8', errors='ignore')
list_hash = []
flag_hash_line = 0
while 1:
    line_hash = f_count_hash.readline()
    if not line_hash:
        break
    else:
        rule1 = r"'(.*?)'"
        rule2 = r'"(.*?)"'
        rule3 = r' (.*?)\)'
        try:
            slotList = re.findall(rule1, line_hash)
            hash_num = re.findall(rule3, line_hash)
            if int(hash_num[0]) == 4:
                break
            else:
                list_hash.append(str(slotList[0]))
                flag_hash_line += 1
        except IndexError:
            slotList = re.findall(rule2, line_hash)
            list_hash.append(str(slotList[0]))
            flag_hash_line += 1

print(flag_hash_line)

list_id = get_list_or_dict('list_id.txt')
print(len(list_id))
dict_id_hash = get_list_or_dict('dict_id_hash.txt')
print(len(dict_id_hash))

f_id_hash = open("id_hash", 'w', encoding='utf8', errors='ignore')
f_id_error = open("id_error", 'w', encoding='utf8', errors='ignore')
i = 0
for id in list_id:
    id = str(id).replace('.mp4', '')
    # print(id)
    line_list_hash = dict_id_hash[id].split(' ')
    # print(line_list_hash)
    line_hash_new = ''
    for hash in line_list_hash:
        hash = str(hash).replace('#', '')
        if hash in list_hash:
            line_hash_new += '#' + hash + ' '
    if line_hash_new == '':
        f_id_error.write(id+'\n')
    else:
        f_id_hash.write(id+'::::'+line_hash_new+'\n')
        i += 1
    if (i % 10000 == 0):
        print(i)
f_id_hash.close()
f_id_error.close()
print(i)
