# 统计hash总数与词频
import collections
import re
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
        elif copy:
            str = str + s
        if finished:
            if str != "":
                slotList.append(str)
            str = ""
            finished = False
    return slotList

slotList = []
i=1
# for i in range(0,5):
while 1:
    line_id_hash = f_id_hash_final.readline()
    if not line_id_hash:
        break
    else:
        slotList += subString1(line_id_hash) #将所有HashTag存进list
# print(slotList)

result = collections.Counter(slotList)  #词频统计
#ss = str(result)    #词频统计结果转换成字符串并存文件
# f_handle_hash.write(ss)
#print(result.most_common(100)) 查看统计结果前100名
for each in result.most_common():
    ss = str(each)    #词频统计结果转换成字符串并存文件
    f_count_hash.write(ss+'\n')
    #print(ss)
f_id_hash_final.close()
f_count_hash.close()