import re
import os
import shutil

def get_id(template):
    rule = r'(.*?)::::'
    slot_list = re.findall(rule, template)
    return slot_list


def get_list_or_dict(path):
    f = open(path, encoding='utf8', errors='ignore')
    a = f.read()
    dict_or_list = eval(a)
    f.close()
    return dict_or_list

dict_id_num = get_list_or_dict('dict_id_num.txt')
print(len(dict_id_num))

list_id_error = []
f_id_error = open('id_error', encoding='utf8', errors='ignore')
while 1:
    line_id_error = f_id_error.readline()
    if not line_id_error:
        break
    else:
        list_id_error.append(dict_id_num[line_id_error.replace('\n','')])
print(len(list_id_error))

path = '/home/caoda/Hodge_work_space/dataset/dataset'
ii = 0
for i in range(1, 16):
    list_extract_num = os.listdir(path + str(i))
    for num in list_extract_num:
        if(num in list_id_error):
            try:
                shutil.rmtree(path+str(i)+'/'+num)
                # print(path+str(i)+'/'+num)
            except:
                print('删除出错')
    ii += len(os.listdir(path + str(i)))
print(ii)