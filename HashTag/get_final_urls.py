import re
#根据count_hash.txt和id_hash_final.txt获得最终需要的一定数量的数据集final_id_texts/hashs/urls.txt
f_dict_id_text_final = open("dict_id_text_final.txt",encoding='utf8', errors='ignore')
f_dict_id_hash_final = open("dict_id_hash_final.txt",encoding='utf8', errors='ignore')
f_list_count_hash = open("list_count_hash.txt",encoding='utf8', errors='ignore')
f_dict_id_url = open("dict_id_url.txt",encoding='utf8', errors='ignore')
f_final_texts = open("final_texts.txt",'w',encoding='utf8', errors='ignore')
f_final_hashs = open("final_hashs.txt",'w',encoding='utf8', errors='ignore')
f_final_urls = open("final_urls.txt",'w',encoding='utf8', errors='ignore')

def getText(template):
    rule = r'::::(.*?)\n'
    slotList = re.findall(rule, template)
    return slotList

def getId(template):
    rule = r'(.*?)::::'
    slotList = re.findall(rule, template)
    return slotList

list_hash = []
f = open("list_count_hash.txt",encoding='utf8', errors='ignore')
a = f.read()
list_hash = eval(a)
f.close()
print("list_count_hash读取成功\n")
print(len(list_hash))

dict_id_text_final = {}
f = open("dict_id_text_final.txt",encoding='utf8', errors='ignore')
a = f.read()
dict_id_text_final = eval(a)
f.close()
print("dict_id_text_final读取成功\n")

dict_id_hash_final = {}
f = open("dict_id_hash_final.txt",encoding='utf8', errors='ignore')
a = f.read()
dict_id_hash_final = eval(a)
f.close()
print("dict_id_hash_final读取成功\n")

dict_id_url = {}
f = open("dict_id_url.txt",encoding='utf8', errors='ignore')
a = f.read()
dict_id_url = eval(a)
f.close()
print("dict_id_url读取成功\n")

print("开始匹配")
list_del = []
iii=0
for hash in list_hash:
    ii = 0
    for key in dict_id_hash_final:
        if (str("#"+hash+" ") in str(dict_id_hash_final[key])):
            f_final_texts.write(key + '::::' + dict_id_text_final[key] + '\n')
            f_final_hashs.write(key + '::::' + dict_id_hash_final[key] + '\n')
            f_final_urls.write(key + '::::' + dict_id_url[key] + '\n')
            ii+=1
            list_del.append(key)
    for i_del in list_del:
        del dict_id_hash_final[i_del]
    list_del = []
    iii+=ii
    print(str(hash)+"--匹配结束，其写入--"+str(ii)+'--条--共计写入'+str(iii)+'条')
    if (str(hash) == 'premiosjuventud'):
        break

f_dict_id_text_final.close()
f_dict_id_hash_final.close()
f_list_count_hash.close()
f_dict_id_url.close()
f_final_texts.close()
f_final_hashs.close()
f_final_urls.close()
