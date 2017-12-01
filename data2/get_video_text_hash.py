#得到带hash的视频描述
f_video_text = open("location_videos_description",encoding='utf8', errors='ignore')
f_video_text_hash = open("video_text_hash.txt",'w',encoding='utf8', errors='ignore')

e = '#'
while 1:
    line_video_text = f_video_text.readline()
    if not line_video_text:
        break
    if (e in line_video_text):
        f_video_text_hash.write(line_video_text)


f_video_text.close()