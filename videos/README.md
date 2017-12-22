###### get_videos_list.py
扫描存放所有视频的文件夹，将所有视频名存储为list_videos_name并写入文件list_videos.txt
###### get_dict_id_text.py
为了获取视频text，须对之前处理获得的final_texts.txt读取获得dict_id_text并存储为dict_id_text.txt
同时为了将视频文件夹从0开始重命名，还要生成dict_id_num并存储为dict_id_num.txt
###### get_final_dataset.py
运行前记得配置video_path和root_path内容

- extract_ok.txt：记录所有处理成功的视频
- extract_ok_this_time.txt：记录每次任务处理成功的视频
- video_error.txt：记录所有处理失败的视频
- video_error_this_time.txt：记录每次任务处理失败的视频

相关数据处理逻辑及代码说明见：[vine数据集处理](https://hodgeli.github.io/2017/11/30/handle-tag/ "blog")