#对于final_hashs1.txt每条item清除频率少于5次的hash
import re
f_final_hashs1 = open("final_hashs1.txt", encoding='utf8', errors='ignore')
f_list_hash = open("count_hash.txt", encoding='utf8', errors='ignore')
f_final_hashs = open("final_hashs.txt", 'w', encoding='utf8', errors='ignore')

def getText(template):
    rule = r'::::(.*?)\n'
    slotList = re.findall(rule, template)
    return slotList

def getId(template):
    rule = r'(.*?)::::'
    slotList = re.findall(rule, template)
    return slotList

list_hash = []
# for i in range(0,5):
while 1:
    line_id_hash = f_list_hash.readline()
    if not line_id_hash:
        break
    else:
        rule = r"'(.*?)'"
        list_hash += re.findall(rule, line_id_hash)
print('list_hash生成成功')

# for i in range(0,100):
i=0
while 1:
    line_hashs = f_final_hashs1.readline()
    list_hashs = []
    str_hashs = ''
    if not line_hashs:
        break
    else:
        try:
            # str_hashs = str(getId(line_hashs)[0]) + '::::'
            rule = r"#(.*?) "
            list_hashs += re.findall(rule, line_hashs)
            for hash in list_hashs:
                if str(hash) in list_hash:
                    str_hashs += '#' + str(hash) + ' '
            if(str_hashs != ''):
                f_final_hashs.write(str(getId(line_hashs)[0]) + '::::'+str_hashs + '\n')
            else:
                print('------')
            i+=1
        except IndexError:
            print("erro")
    if(i%10000==0):
        print(i)

f_final_hashs1.close()
f_list_hash.close()
f_final_hashs.close()