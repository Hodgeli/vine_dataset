# 首先配置video_path和root_path内容
import os
import subprocess
import json


def mkdir(path):
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("/")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)

        # print(str(path) + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        # print(str(path) + ' 目录已存在')
        return False


def get_lines(file_name):
    count = 0
    thefile = open(file_name, encoding='utf8', errors='ignore')
    while True:
        buffer = thefile.read(1024 * 8192)
        if not buffer:
            break
        count += buffer.count('\n')
    thefile.close()
    return count


def get_time(filename):
    command = 'ffprobe -loglevel quiet -print_format json -show_format -show_streams -i ' + filename
    result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    out = result.stdout.read()

    temp = str(out.decode('utf-8'))
    data = json.loads(temp)["format"]['duration']
    return data


def get_flag_list(flag):
    list_flag = []
    while flag:
        get_num = flag % 10
        list_flag.append(int(get_num))
        flag = (flag - get_num) / 10
    return list_flag

def file_name(file_dir):  # 获取视频名list
    for root, dirs, files in os.walk(file_dir):
        continue
    return files

f_list_videos = open("list_videos.txt", encoding='utf8', errors='ignore')
a = f_list_videos.read()
list_videos = eval(a)
f_list_videos.close()
print('list_videos.txt读取成功')

f_extract_ok = open("extract_ok.txt", 'a', encoding='utf8', errors='ignore')
f_extract_ok_this_time = open("extract_ok_this_time.txt", encoding='utf8', errors='ignore')
while 1:
    line_extract_ok_this_time = f_extract_ok_this_time.readline()
    if not line_extract_ok_this_time:
        break
    else:
        list_videos.remove(str(line_extract_ok_this_time.split(' ')[0]).replace('\n', '') + '.mp4')  # 更新未抽取videos
        f_extract_ok.write(str(line_extract_ok_this_time))  # 更新已抽取videos
f_extract_ok_this_time.close()
f_extract_ok.close()

print("list_videos清理已抽取视频id成功")
print("extract_ok添加已抽取视频id成功")

print("总共已抽取" + str(get_lines('extract_ok.txt')) + '条视频')

f = open("extract_ok_this_time.txt", 'w', encoding='utf8', errors='ignore')  # 释放空间
f.close()

f_video_error = open("video_error.txt", 'a', encoding='utf8', errors='ignore')
f_video_error_this_time = open("video_error_this_time.txt", encoding='utf8', errors='ignore')
while 1:
    line_video_error_this_time = f_video_error_this_time.readline()
    if not line_video_error_this_time:
        break
    else:
        list_videos.remove(str(line_video_error_this_time.split(' ')[0]).replace('\n', '') + '.mp4')  # 更新未抽取videos
        f_video_error.write(str(line_video_error_this_time))  # 更新失败videos
f_video_error_this_time.close()
f_video_error.close()
f_list_videos = open("list_videos.txt", 'w', encoding='utf8', errors='ignore')
f_list_videos.write(str(list_videos))
f_list_videos.close()

print("list_videos清理出错视频id成功")
print("video_error增加错误videos成功")
print("共有" + str(get_lines('video_error.txt')) + '条视频抽取错误')

print("共剩余" + str(len(list_videos)) + '条未抽取')

f = open("video_error_this_time.txt", 'w', encoding='utf8', errors='ignore')  # 释放空间.
f.close()

f = open("dict_id_text.txt", encoding='utf8', errors='ignore')
a = f.read()
dict_id_text = eval(a)
f.close()
print("dict_id_text读取成功")

f = open("dict_id_num.txt", encoding='utf8', errors='ignore')
a = f.read()
dict_id_num = eval(a)
f.close()
print("dict_id_num读取成功\n")

print('---开始抽取---')
# print(list_videos)
flag_num = 1
for video_name in list_videos:
    try:
        video_path = '/home/caoda/Hodge_work_space/videos_data/videos_20171208/' + str(video_name)  # 配置视频文件夹路径
        video_name = video_name.replace(".mp4", "")
        video_num = dict_id_num[str(video_name)]

        root_path = '/home/caoda/Hodge_work_space/dataset/dataset2/'
        mkpath_images = root_path + video_num + '/images'  # 路径全英文---存12帧图片文件夹路径
        mkdir(mkpath_images)
        mkpath_audios = root_path + video_num + '/audios'  # 路径全英文---存音频文件夹路径
        mkdir(mkpath_audios)
        mkpath_texts = root_path + video_num + '/texts'  # 路径全英文---存文本文件夹路径
        mkdir(mkpath_texts)

        # video_time = get_time(video_path)
        # time_flag = 12.0 / float(video_time)
        #
        # cmd = r'ffmpeg -i ' + video_path + ' -r ' + str(
        #     time_flag) + ' -vframes 12 ' + mkpath_images + '/%02d.jpg -loglevel quiet -y'
        # os.system(cmd)
        video_time = get_time(video_path)
        list_time = [12, 6, 4, 3, 3, 2, 2]
        time_flag = int(float(video_time))

        cmd = r'ffmpeg -i ' + video_path + ' -r ' + str(
            list_time[time_flag - 1]) + ' -vframes 12 ' + mkpath_images + '/%d.jpg -loglevel quiet -y'
        # print(cmd)
        os.system(cmd)
        # time.sleep(0.3)

        audio_path = mkpath_audios + '/' + video_name + '.mp3'
        cmd = 'ffmpeg -i ' + video_path + ' -f mp3 -vn ' + audio_path + ' -loglevel quiet -y'
        os.system(cmd)  # 提取音频
        # print(video_path + '\n' + mkpath_images + '\n' + audio_path + '\n')
        video_time = get_time(video_path)  # 音频分段
        video_time = int(float(video_time) * 1000)
        flag = int(video_time / 6)
        list_flag = get_flag_list(flag)
        every_time = str(list_flag[2]) + str(list_flag[1]) + str(list_flag[0])
        start = 0
        end = flag
        for i in range(1, 7):
            cmd = 'ffmpeg -y -i ' + audio_path + ' -ss 00:00:0' + str(int(start / 1000)) + '.' + str(
                int(start % 1000)) + ' -t 00:00:0' + str(
                int(
                    flag / 1000)) + '.' + every_time + ' -codec copy ' + mkpath_audios + '/' + str(
                i) + '.mp3' + ' -loglevel quiet'
            # print(cmd)
            os.system(cmd)
            start += flag
            end += flag

        image_num = len(file_name(mkpath_images))
        audio_num = len(file_name(mkpath_audios))
        if(image_num == 12 and audio_num == 7):
            f_video_text = open(mkpath_texts + '/text.txt', 'w', encoding='utf8', errors='ignore')
            f_video_text.write(str(dict_id_text[video_name]) + '\n')
            f_video_text.close()
            print(flag_num)
            f_extract_ok_this_time = open("extract_ok_this_time.txt", 'a', encoding='utf8', errors='ignore')
            f_extract_ok_this_time.write(str(video_name) +' '+video_num+ '\n')
            f_extract_ok_this_time.close()
            flag_num += 1
    except (TimeoutError,KeyError,IndexError):
        print('----video打开失败----')
        f_video_error_this_time = open("video_error_this_time.txt", 'a', encoding='utf8', errors='ignore')
        f_video_error_this_time.write(str(video_name) +' '+video_num+ '\n')
        f_video_error_this_time.close()
        print('本次已抽取' + str(get_lines('extract_ok_this_time.txt')) + '条，本次抽取videos错误' + str(
            get_lines('video_error_this_time.txt')) + '条')
        # print(dict_video_error_this_time)
        print('已保存并跳过此条video_id，抽取继续-->')
    # if (flag_num % 500 == 0):
    #     print('本次已抽取' + str(flag_num) + '条视频')
print("****抽取完成****")