# 获取要提取关键帧的所有视频的名字存储在list_videos_name并写入文件list_videos_name.txt
import os


def file_name(file_dir):  # 获取视频名list
    for root, dirs, files in os.walk(file_dir):
        continue
    return files


videos_path = '/home/hodge/work_space/videos/videos_example'  # 填写存放视频的文件夹路径
list_videos_name = file_name(videos_path)

f_list_videos_name = open("list_videos.txt", 'w', encoding='utf8', errors='ignore')
f_list_videos_name.write(str(list_videos_name))
f_list_videos_name.close()
