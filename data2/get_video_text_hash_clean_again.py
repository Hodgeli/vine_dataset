import re
#将video_text_hash_off_cover.txt依据video_url_off.txt清除缺失url项
f1_video_text = open("video_url_off.txt",encoding='utf8', errors='ignore')
# f1_video_text = open("test1.txt",encoding='gb18030', errors='ignore')
f2_video_text = open("video_text_hash_off_cover.txt",encoding='utf8', errors='ignore')
# f2_video_text = open("test2.txt",encoding='gb18030', errors='ignore')
f_video_text_hash = open("video_text_hash_4.txt",'w',encoding='utf8', errors='ignore')

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
        #each_id = getId(line_video_text)
        rule = r'(.*?)\n'
        slotList = re.findall(rule, line_video_text)
        list_1.append(slotList[0])
#print(list_1)      #data1的id  list

dict_2 = {}
list_2 = []
ii=1
while 1:
    line_video_text = f2_video_text.readline()
    if not line_video_text:
        break
    else:
        each_id = getId(line_video_text)
        each_text = getText(line_video_text)
        dict_2[each_id[0]] = each_text[0]
        list_2.append(each_id[0])
    ii += 1
    if (ii % 10000 == 0):
        print(ii)
#print(list_2[0])     #data2的dict {id:text}

ii=0
for i in list_2:
    if(i in list_1):
        pass
    else:
        f_video_text_hash.write(i + ':::' + dict_2[i] + '\n')
    ii += 1
    if (ii % 10000 == 0):
        print(ii)

f1_video_text.close()
f2_video_text.close()
f_video_text_hash.close()