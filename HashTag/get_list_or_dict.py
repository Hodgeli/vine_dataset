import re
#id_text_final-->dict_id_text_final
#id_hash_final-->dict_id_hash_final
#count_hash-->list_count_hash
#video_url_hash-->dict_id_url
f_id_text_final = open("id_text_final.txt",encoding='utf8', errors='ignore')
f_dict_id_text_final = open("dict_id_text_final.txt",'w',encoding='utf8', errors='ignore')
f_id_hash_final = open("id_hash_final.txt",encoding='utf8', errors='ignore')
f_dict_id_hash_final = open("dict_id_hash_final.txt",'w',encoding='utf8', errors='ignore')
f_count_hash = open("count_hash.txt",encoding='utf8', errors='ignore')
f_list_count_hash = open("list_count_hash.txt",'w',encoding='utf8', errors='ignore')
f_video_url_hash = open("video_url_hash.txt",encoding='utf8', errors='ignore')
f_dict_id_url = open("dict_id_url.txt",'w',encoding='utf8', errors='ignore')

def getText(template):
    rule = r'::::(.*?)\n'
    slotList = re.findall(rule, template)
    return slotList

def getId(template):
    rule = r'(.*?)::::'
    slotList = re.findall(rule, template)
    return slotList

list_hash = []
while 1:
    line_hash = f_count_hash.readline()
    if not line_hash:
        break
    else:
        rule1 = r"'(.*?)'"
        rule2 = r'"(.*?)"'
        try:
            slotList = re.findall(rule1, line_hash)
            list_hash.append(str(slotList[0]))
        except IndexError:
            slotList = re.findall(rule2, line_hash)
            list_hash.append(str(slotList[0]))
f_list_count_hash.write(str(list_hash))
# print(len(list_1))      #data1的id  list

dict_id_text_final = {}
dict_id_hash_final = {}
ii=1
while 1:
    line_id_text = f_id_text_final.readline()
    line_id_hash = f_id_hash_final.readline()
    if not line_id_text:
        break
    else:
        each_id = getId(line_id_text)
        each_text = getText(line_id_text)
        dict_id_text_final[each_id[0]] = each_text[0]
        each_id = getId(line_id_hash)
        each_text = getText(line_id_hash)
        dict_id_hash_final[each_id[0]] = each_text[0]
    ii += 1
    if (ii % 50000 == 0):
        print(ii)
f_dict_id_text_final.write(str(dict_id_text_final))
f_dict_id_hash_final.write(str(dict_id_hash_final))
# print(dict_id_text_final['980744748887429120'])     #data2的dict {id:text}
# print(dict_id_hash_final['980744748887429120'])

dict_id_url = {}
ii=1
while 1:
    line_id_url = f_video_url_hash.readline()
    if not line_id_url:
        break
    else:
        each_id = getId(line_id_url)
        each_text = getText(line_id_url)
        dict_id_url[each_id[0]] = each_text[0]
    ii += 1
    if (ii % 50000 == 0):
        print(ii)
f_dict_id_url.write(str(dict_id_url))
# print(dict_id_url['980744748887429120'])     #data2的dict {id:text}

f_id_text_final.close()
f_dict_id_text_final.close()
f_id_hash_final.close()
f_dict_id_hash_final.close()
f_count_hash.close()
f_list_count_hash.close()
f_video_url_hash.close()
f_dict_id_url.close()
