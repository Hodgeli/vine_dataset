# 获取所有拆分成功的短视频id存入list_id.txt
import os


def file_name(file_dir):  # 获取视频名list
    for root, dirs, files in os.walk(file_dir):
        continue
    return files


path = '/home/caoda/Hodge_work_space/videos_data/videos_201712'
list_id = []
f_list_id = open("list_id.txt", encoding='utf8', errors='ignore')
a = f_list_id.read()
list_id = eval(a)
f_list_id.close()

print('读取list_id成功，现有' + str(len(list_id)) + '条数据')
list_path = ['07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '18', '19', '20', '21', '24']
for i in list_path:
    list_id += file_name(path + i)
    # print(path + str(i))

print('总视频数：' + str(len(list_id)))  # 121117条数据-下载失败条数
# 去除提取失败与剩余条数

f_extract_fail = open("extract_fail", encoding='utf8', errors='ignore')
i = 0
while 1:
    line_extract_fail = f_extract_fail.readline()
    if not line_extract_fail:
        break
    else:
        line_extract_fail = line_extract_fail.replace('\n', '')
        if (line_extract_fail in list_id):
            list_id.remove(line_extract_fail)
            i += 1

print('清理' + str(i) + '条数据\n最后总数据' + str(len(list_id)))

f_list_id = open("list_id.txt", 'w', encoding='utf8', errors='ignore')
f_list_id.write(str(list_id))
f_list_id.close()

list_id.clear()
