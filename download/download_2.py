# 可间断性地下载final_urls.txt的链接获得视频集
import urllib.request
import re

def getLines(file_name):  # 获取文件行数
    count = 0
    thefile = open(file_name, encoding='utf8', errors='ignore')
    while True:
        buffer = thefile.read(1024 * 8192)
        if not buffer:
            break
        count += buffer.count('\n')
    thefile.close()
    return count

def get_id(template):
    rule = r'(.*?)::::'
    slotList = re.findall(rule, template)
    return slotList

# dict_id_url = {}
f = open("dict_id_url.txt", encoding='utf8', errors='ignore')
a = f.read()
dict_id_url = eval(a)
f.close()
print("dict_id_url读取成功")  # 读取剩余urls

f_down_ok = open("down_ok.txt", 'a', encoding='utf8', errors='ignore')
f_down_ok_this_time = open("down_ok_this_time.txt", encoding='utf8', errors='ignore')
while 1:
    line_down_ok_this_time = f_down_ok_this_time.readline()
    if not line_down_ok_this_time:
        break
    else:
        line_down_ok_this_time = line_down_ok_this_time.replace('\n', '')
        del dict_id_url[str(line_down_ok_this_time)]  # 更新未下载urls
        f_down_ok.write(str(line_down_ok_this_time) + '\n')  # 更新已下载urls
f_down_ok_this_time.close()
f_down_ok.close()

print("dict_id_url清理已下载urls成功")
print("down_ok添加已下载urls成功")


print("总共已下载" + str(getLines('down_ok.txt')) + '条视频')

f = open("down_ok_this_time.txt", 'w', encoding='utf8', errors='ignore')  # 清空文本
f.close()

f_url_error = open("url_error.txt", 'a', encoding='utf8', errors='ignore')
f_url_error_this_time = open("url_error_this_time.txt", encoding='utf8', errors='ignore')
while 1:
    line_url_error_this_time = f_url_error_this_time.readline()
    if not line_url_error_this_time:
        break
    else:
        del dict_id_url[str(get_id(line_url_error_this_time)[0])]  # 更新未下载urls
        f_url_error.write(str(line_url_error_this_time))  # 更新失效urls
f_url_error_this_time.close()
f_url_error.close()

f_dict_id_url = open("dict_id_url.txt", 'w', encoding='utf8', errors='ignore')  # 保存未下载的urls
f_dict_id_url.write(str(dict_id_url))
f_dict_id_url.close()

print("dict_id_url清理下载错误urls成功")
print("共剩余" + str(len(dict_id_url)) + '条未下载')
print("url_error增加错误urls成功")
print("共有" + str(getLines('url_error.txt')) + '条视频链接错误')

f = open("url_error_this_time.txt", 'w', encoding='utf8', errors='ignore')  # 清空文本
f.close()

print('---开始下载---')
flag = 1
for key in dict_id_url:
    url = str(dict_id_url[key])
    try:
        if '.mp4?' in url:
            # video_name = "e:\\videos\\" + str(key)+'.mp4'     #视频保存路径d:\videos
            video_name = "d:\\test\\" + str(key) + '.mp4'  # 视频保存路径d:\videos
            urllib.request.urlretrieve(url, video_name)  # 下载
            f_down_ok_this_time = open("down_ok_this_time.txt", 'a', encoding='utf8', errors='ignore')
            f_down_ok_this_time.write(str(key) + '\n')
            f_down_ok_this_time.close()
            print(str(getLines('down_ok_this_time.txt')))  # 下载成功一条打一个标记
            flag += 1
        else:
            f_url_error_this_time = open("url_error_this_time.txt", 'a', encoding='utf8', errors='ignore')
            f_url_error_this_time.write(str(key) + '::::' + dict_id_url[key] + '\n')
            f_url_error_this_time.close()
    except (TimeoutError, urllib.error.URLError):
        print('----url失效，下载超时----')
        f_url_error_this_time = open("url_error_this_time.txt", 'a', encoding='utf8', errors='ignore')
        f_url_error_this_time.write(str(key) + '::::' + dict_id_url[key] + '\n')
        f_url_error_this_time.close()
        print('本次已下载' + str(getLines('down_ok_this_time.txt')) + '条，本次下载url错误' + str(
            getLines('url_error_this_time.txt')) + '条')
        print('已保存并跳过此条url，下载继续-->')
# if(flag%1000==0):
#         print('本次已下载'+str(flag)+'条视频')
print("****下载全部完成****")
# print('一共下载' + str(len(list_down_ok)) + '条，错误' + str(len(dict_url_error)) + '条')
