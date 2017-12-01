import re
#根据video_text_hash_off_cover.txt清洗video_url.txt
f1_video_text = open("video_text_hash_off_cover.txt",encoding='utf8', errors='ignore')
# f1_video_text = open("test1.txt",encoding='gb18030', errors='ignore')
f2_video_text = open("video_url.txt",encoding='utf8', errors='ignore')
# f2_video_text = open("test2.txt",encoding='gb18030', errors='ignore')
f_video_url_hash = open("video_url_hash.txt",'w',encoding='utf8', errors='ignore')
f_video_url_off = open("video_url_off.txt",'w',encoding='utf8', errors='ignore')

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
ii=1
dict_2 = {}
while 1:
    line_video_text = f2_video_text.readline()
    if not line_video_text:
        break
    else:
        each_id = getId(line_video_text)
        each_text = getText(line_video_text)
        dict_2[each_id[0]] = each_text[0]
        ii += 1
        if (ii % 5000 == 0):
            print(ii)

#print(dict_2)     #data2的dict {id:text}
print("开始清洗")
ii=1
for i in list_1:
    if(i in dict_2):
        try:
            f_video_url_hash.write(i + '::::' + dict_2[i] + '\n')
        except IndexError:
            print("c1")
    else:
        try:
            f_video_url_off.write(i + '\n')
        except IndexError:
            print("c2")
    ii+=1
    if(ii%5000==0):
        print(ii)



f1_video_text.close()
f2_video_text.close()
f_video_url_hash.close()