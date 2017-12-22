#每次任务收尾工作
import shutil

f = open("dict_id_num.txt", encoding='utf8', errors='ignore')
a = f.read()
dict_id_num = eval(a)
f.close()
print("dict_id_num读取成功")

f_list_videos = open("list_videos.txt", encoding='utf8', errors='ignore')
a = f_list_videos.read()
list_rest = eval(a)
f_list_videos.close()
print('list_rest.txt读取成功')


f_video_error = open("video_error.txt", encoding='utf8', errors='ignore')
root_path = '/home/caoda/Hodge_work_space/dataset/dataset2/'
while 1:
    line_video_error = f_video_error.readline()
    if not line_video_error:
        break
    else:
        try:
            error_id = dict_id_num[line_video_error.split(' ')[0]]
            # print(root_path+error_id)
            shutil.rmtree('/home/caoda/Hodge_work_space/dataset/dataset2/' + error_id)
        except(FileNotFoundError):
            print('文件夹不存在')
f.close()
print("删除error videos成功\n")

for rest_video in list_rest:
    try:
        error_id = dict_id_num[rest_video.split('.')[0]]
        # print(root_path + error_id)
        shutil.rmtree('/home/caoda/Hodge_work_space/dataset/dataset2/' + error_id)
    except(FileNotFoundError):
        print('文件夹不存在')
print('删除rest videos成功')
#
# f_list_videos = open("list_videos.txt",'w', encoding='utf8', errors='ignore')
# f_list_videos.close()
# print('f_list_videos.txt清空成功')
#
# f_video_error = open("video_error.txt", 'w',encoding='utf8', errors='ignore')
# f_video_error.close()
# print('f_video_error.txt清空成功')






