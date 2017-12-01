# 统计hash总数与词频
import collections
#f_video_text_hash = open("test.txt", encoding='gb18030', errors='ignore')
f_video_text_hash = open("video_text_hash.txt", encoding='utf8', errors='ignore')
f_handle_hash = open("handle_hash.txt", 'w', encoding='utf8', errors='ignore')


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

slotList = []
i=1
while 1:
    line_video_text = f_video_text_hash.readline()
    if not line_video_text:
        break
    else:
        slotList += subString1(line_video_text) #将所有HashTag存进list

result = collections.Counter(slotList)  #词频统计
#ss = str(result)    #词频统计结果转换成字符串并存文件
# f_handle_hash.write(ss)
#print(result.most_common(100)) 查看统计结果前100名
for each in result.most_common():
    ss = str(each)    #词频统计结果转换成字符串并存文件
    f_handle_hash.write(ss+'\n')
    #print(ss)
f_video_text_hash.close()
f_handle_hash.close()