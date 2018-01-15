import re
import os


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


def file_name(file_dir):  # 获取视频名list
    for root, dirs, files in os.walk(file_dir):
        continue
    return files


def is_alpha(word):
    try:
        return word.encode('ascii').isalpha()
    except UnicodeEncodeError:
        return False


f_stop_word = open("stop_word.txt", encoding='utf8', errors='ignore')
list_stop_word = []
while 1:
    line_stop_word = f_stop_word.readline()
    if not line_stop_word:
        break
    else:
        list_stop_word.append(str(line_stop_word).replace("\n", '').lower())
print("停用词列表生成成功:" + str(len(list_stop_word)))

list_hash_down = file_name(r'I:\推荐系统\数据集\twitter\hash_twitter')
print(len(list_hash_down))

for hash in list_hash_down:
    f_twitter = open('./hash_twitter/' + hash, encoding='utf8', errors='ignore')
    long_str = ''
    # for i in range(1, 10):
    while 1:
        line_twitter = f_twitter.readline()
        if not line_twitter:
            break
        else:
            line_twitter = re.sub(r'#\w* ', '', line_twitter)
            line_twitter = re.sub(r'#\w*\n', '', line_twitter)
            line_twitter = re.sub(r'https\S* ', '', line_twitter)
            line_twitter = re.sub(r'https\S*\n', '', line_twitter)
            text_final = ''
            for s in line_twitter:
                if is_alpha(s):
                    text_final += s
                elif s == ' ' or s == '-' or s == '~':
                    text_final += ' '  # 去除非英文字符，保留空格
            text_final = re.sub(r'\s+', ' ', text_final)
            line_twitter = text_final.lower()
            list_word = line_twitter.split(' ')  # 分词，包含空字符
            text_final = ''
            for word in list_word:
                if word == '':
                    continue
                elif word not in list_stop_word:  # 去除中止词
                    text_final += word + ' '
            long_str += text_final
    f_twitter.close()
    long_str = re.sub(r'\n', '', long_str)
    long_str = re.sub(r'\s+', ' ', long_str)
    list_word = long_str.split(' ')
    if (len(list_word) < 10):
        print(str(hash) + '太短')
        f_short_result = open('short_result', 'a', encoding='utf8', errors='ignore')
        f_short_result.write(str(hash) + '\n')
        f_short_result.close()
    else:
        f_twitter_new = open('./hash_twitter_new/' + hash, 'w', encoding='utf8', errors='ignore')
        f_twitter_new.write(long_str)
        f_twitter_new.close()
