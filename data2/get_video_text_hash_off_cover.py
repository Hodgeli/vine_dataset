import re
#data1与data2的video_text_hash去重
f1_video_text = open("video_text_hash_1.txt",encoding='utf8', errors='ignore')
# f1_video_text = open("test1.txt",encoding='gb18030', errors='ignore')
f2_video_text = open("video_text_hash_2.txt",encoding='utf8', errors='ignore')
# f2_video_text = open("test2.txt",encoding='gb18030', errors='ignore')
f_video_text_hash = open("video_text_hash_3.txt",'w',encoding='utf8', errors='ignore')
f_video_text_cover = open("video_cover.txt",'w',encoding='utf8', errors='ignore')

def getText(template):
    rule = r':::(.*?)\n'
    slotList = re.findall(rule, template)
    return slotList

def getId(template):
    rule = r'(.*?):::'
    slotList = re.findall(rule, template)
    return slotList

list_1 = []
while 1:
    line_video_text = f1_video_text.readline()
    if not line_video_text:
        break
    else:
        each_id = getId(line_video_text)
        list_1.append(each_id[0])
#print(list_1)      #data1的id  list

dict_2 = {}
i=1
while 1:
    line_video_text = f2_video_text.readline()
    if not line_video_text:
        break
    else:
        each_id = getId(line_video_text)
        each_text = getText(line_video_text)
        dict_2[each_id[0]] = each_text[0]


#print(dict_2)     #data2的dict {id:text}

for key in dict_2:
    if(key not in list_1):
        f_video_text_hash.write(key + '::' + dict_2[key] + '\n')
    else:
        f_video_text_cover.write(key + '::' + dict_2[key] + '\n')
    i+=1
    if(i%1000==0):
        print(i)



f1_video_text.close()
f2_video_text.close()
f_video_text_hash.close()