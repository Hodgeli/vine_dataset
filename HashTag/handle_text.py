import re
#根据video_text_hash.txt将hash提取出来获得id_hash.txt和剩下的id_text.txt其中排除剩余为空的id_text_void.txt
f_video_texts = open("video_text_hash.txt",encoding='utf8', errors='ignore')
f_text = open("id_text.txt",'w',encoding='utf8', errors='ignore')
f_text_void = open("id_text_void.txt",'w',encoding='utf8', errors='ignore')
f_hash = open("id_hash.txt",'w',encoding='utf8', errors='ignore')

def get_hashs(template):  # HashTag以‘#’开头，以空格或回车结尾
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
        elif s == '\n':
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

def getText(template):
    rule = r'::::(.*?)\n'
    slotList = re.findall(rule, template)
    return slotList

def getId(template):
    rule = r'(.*?)::::'
    slotList = re.findall(rule, template)
    return slotList

# for i in range(1,20):
ii=0
while 1:
    line_video_text = f_video_texts.readline()
    list_hash = []
    if not line_video_text:
        break
    else:
        try:
            list_hash = get_hashs(line_video_text)
            list_text = getText(line_video_text)
            # print(list_text)
            # print(list_hash)
            str_text = str(list_text[0])+'\n'
            # print(str_text)
            str_hashs = ''
            for hash in list_hash:
                str_hash1 = '#'+str(hash)+' '
                str_hashs += str(str_hash1)
                str_hash2 = '#' + str(hash) + '\n'
                str_text = str_text.replace(str_hash1,"")
                str_text = str_text.replace(str_hash2, "\n")
            # print(str_text)
            # print(list_hash)
        except IndexError:
            print("error")
        # print(str_text)
        if(str_text != '\n'):
            f_text.write(str(getId(line_video_text)[0])+'::::'+str_text.lower())
            f_hash.write(str(getId(line_video_text)[0])+'::::'+str_hashs.lower()+'\n')
        else:
            f_text_void.write(str(getId(line_video_text)[0])+'\n')
    ii+=1
    if(ii%10000==0):
        print(ii)
# print(len(list_1))      #data1的id  list

f_video_texts.close()
f_text.close()
f_text_void.close()
f_hash.close()

