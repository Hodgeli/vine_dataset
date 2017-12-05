import re
#根据id_text.txt做文本处理获得id_text_final.txt和排除剩余为空的id_text_final_void.txt
#顺便得到清理后的id::::hashs文件id_hash_final.txt
f_video_texts = open("id_text.txt",encoding='utf8', errors='ignore')
f_stop_word = open("stop_word.txt",encoding='utf8', errors='ignore')
f_id_hash = open("id_hash.txt",encoding='utf8', errors='ignore')
f_id_text_final = open("id_text_final.txt",'w',encoding='utf8', errors='ignore')
f_id_text_final_void = open("id_text_final_void.txt",'w',encoding='utf8', errors='ignore')
f_id_hash_final = open("id_hash_final.txt",'w',encoding='utf8', errors='ignore')

def getText(template):
    rule = r'::::(.*?)\n'
    slotList = re.findall(rule, template)
    return slotList

def getId(template):
    rule = r'(.*?)::::'
    slotList = re.findall(rule, template)
    return slotList

#解决.isalpha()方法对（unicode string，string.isalpha会根据字符串中的字符是否属于Unicode编码的LETTER区域来判断是否都由字母组成。
# 所以得出的结果为True，不一定表示只有26个英文字母。）
def isAlpha(word):
    try:
        return word.encode('ascii').isalpha()
    except UnicodeEncodeError:
        return False

list_stop_word = []
while 1:
    line_stop_word = f_stop_word.readline()
    if not line_stop_word:
        break
    else:
        list_stop_word.append(str(line_stop_word).replace("\n",'').lower())
print("停用词列表生成成功")

dict_hash = {}
while 1:
    line_hash = f_id_hash.readline()
    if not line_hash:
        break
    else:
        dict_hash[getId(line_hash)[0]] = getText(line_hash)[0]
print("hash字典生成成功")

ii=0
# for i in range(1,3):
while 1:
    line_video_text = f_video_texts.readline()
    list_word = []
    if not line_video_text:
        break
    else:
        try:
            list_text = str(getText(line_video_text)[0])
            text_final = ''
            for s in list_text:
                if isAlpha(s):
                    text_final += s
                elif s==' ':
                    text_final += s    #text字符串，包含多余空格
            # print(text_final)
            list_word = text_final.split(' ')   #分词，包含空字符
            text_final = ''
            for word in list_word:
                if word == '':
                    continue
                elif word not in list_stop_word:
                    text_final += word+' '
            if text_final != '':
                str_hash = dict_hash[getId(line_video_text)[0]]     #清除非全英文字母的hash
                rule = r'#(.*?) '
                list_hashs = re.findall(rule, str_hash)
                str_hash = ''
                for hash in list_hashs:
                    flag = 1
                    for s in hash:
                        if isAlpha(s):
                            continue
                        else:
                            flag = 0
                            break
                    if flag:
                        str_hash += '#'+hash+' '
                if str_hash != '':
                    f_id_text_final.write(getId(line_video_text)[0]+'::::'+text_final+'\n')     #将去除空结果的id::::text写入id_text_final.txt
                    f_id_hash_final.write(getId(line_video_text)[0]+'::::'+str_hash+'\n')
            else:
                f_id_text_final_void.write(getId(line_video_text)[0]+'\n')      #将空白结果id写入text_final_void.txt
        except IndexError:
            print("error")
    ii+=1
    if(ii%10000==0):
        print(ii)
# print(len(list_1))      #data1的id  list

f_video_texts.close()
f_stop_word.close()
f_id_hash.close()
f_id_text_final.close()
f_id_text_final_void.close()
f_id_hash_final.close()
