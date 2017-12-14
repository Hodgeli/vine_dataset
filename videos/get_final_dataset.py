# 配置video_path、mkpath_images和mkpath_audios内容
import cv2
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

        print(str(path) + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(str(path) + ' 目录已存在')
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
    command = ["ffprobe.exe", "-loglevel", "quiet", "-print_format", "json", "-show_format", "-show_streams", "-i",
               filename]
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


# list_videos = []
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
        list_videos.remove(str(line_extract_ok_this_time).replace('\n', '') + '.mp4')  # 更新未抽取videos
        f_extract_ok.write(str(line_extract_ok_this_time))  # 更新已抽取videos
f_extract_ok_this_time.close()
f_extract_ok.close()
f_list_videos = open("list_videos.txt", 'w', encoding='utf8', errors='ignore')
f_list_videos.write(str(list_videos))
f_list_videos.close()
print("list_videos清理已抽取视频id成功")
print("extract_ok添加已抽取视频id成功")

print("共剩余" + str(len(list_videos)) + '条未抽取')
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
        f_video_error.write(str(line_video_error_this_time) + '\n')  # 更新失败videos
f_video_error_this_time.close()
f_video_error.close()

print("video_error增加错误videos成功")
print("共有" + str(get_lines('video_error.txt')) + '条视频抽取错误')

f = open("video_error_this_time.txt", 'w', encoding='utf8', errors='ignore')  # 释放空间.
f.close()

f = open("dict_id_text.txt", encoding='utf8', errors='ignore')
a = f.read()
dict_id_text = eval(a)
f.close()
print("dict_id_text读取成功\n")

print('---开始抽取---')
flag = 1
for video_name in list_videos:
    try:
        video_path = 'D:/videos/videos_20171207/' + str(video_name)  # 配置视频文件夹路径
        video_cap = cv2.VideoCapture(video_path)

        frame_count = 0
        all_frames = []
        while (True):
            ret, frame = video_cap.read()
            if ret is False:
                break
            all_frames.append(frame)  # 视频所有帧存list
            frame_count = frame_count + 1  # 帧数

        i = 0
        flag = int(frame_count / 12)
        video_name = video_name.replace(".mp4", "")
        mkpath_images = "I:/images/" + video_name + '/images'  # 路径全英文---存12帧图片文件夹路径
        mkdir(mkpath_images)
        mkpath_audios = "I:/images/" + video_name + '/audios'  # 路径全英文---存音频文件夹路径
        mkdir(mkpath_audios)
        mkpath_texts = "I:/images/" + video_name + '/texts'  # 路径全英文---存文本文件夹路径
        mkdir(mkpath_texts)
        for frame in all_frames:
            i = i + 1
            if (i % flag == 0 and i <= flag * 12):
                path = mkpath_images + '/' + str(int(i / flag)) + '.jpg'
                cv2.imwrite(path, frame)  # 存储为图像
        audio_path = mkpath_audios + '/' + video_name + '.mp3'
        cmd = 'ffmpeg -i ' + video_path + ' -f mp3 -vn ' + audio_path + ' -loglevel quiet -y'
        os.system(cmd)  # 提取音频

        video_time = get_time(video_path)  # 音频分段
        video_time = int(float(video_time) * 1000)
        flag = int(video_time / 6)
        list_flag = get_flag_list(flag)
        every_time = str(list_flag[2]) + str(list_flag[1]) + str(list_flag[0])
        start = 0
        end = flag
        for i in range(1, 7):
            cmd = 'ffmpeg -y -vn -ss 00:00:0' + str(int(start / 1000)) + '.' + str(
                int(start % 1000)) + ' -t 00:00:0' + str(
                int(
                    flag / 1000)) + '.' + every_time + ' -i ' + audio_path + ' -codec copy ' + mkpath_audios + '/' + str(
                i) + '.mp3' + ' -loglevel quiet'
            # print(cmd)
            os.system(cmd)
            start += flag
            end += flag

        f_video_text = open(mkpath_texts+'/text.txt', 'w', encoding='utf8', errors='ignore')
        f_video_text.write(str(dict_id_text[video_name])+'\n')
        f_video_text.close()
        print('。。。。。')
        f_extract_ok_this_time = open("extract_ok_this_time.txt", 'a', encoding='utf8', errors='ignore')
        f_extract_ok_this_time.write(str(video_name) + '\n')
        f_extract_ok_this_time.close()
        flag += 1
    except (TimeoutError):
        print('----video打开失败----')
        f_video_error_this_time = open("video_error_this_time.txt", 'a', encoding='utf8', errors='ignore')
        f_video_error_this_time.write(str(video_name) + '\n')
        f_video_error_this_time.close()
        print('本次已抽取' + str(get_lines('extract_ok_this_time.txt')) + '条，本次抽取videos错误' + str(
            get_lines('video_error_this_time.txt')) + '条')
        # print(dict_video_error_this_time)
        print('已保存并跳过此条video_id，抽取继续-->')
    if (flag % 1000 == 0):
        print('本次已抽取' + flag + '条视频')
print("****下载抽取完成****")
