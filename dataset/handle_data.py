#得到带hash的视频描述与视频链接
f_video_text = open("video_text.txt",encoding='utf8', errors='ignore')
f_video_url = open("video_download_link.txt",encoding='utf8', errors='ignore')
f_video_text_hash = open("video_text_hash.txt",'w',encoding='utf8', errors='ignore')
f_video_url_hash = open("video_url_hash.txt",'w',encoding='utf8', errors='ignore')

e = '#'
while 1:
    line_video_text = f_video_text.readline()
    line_video_url = f_video_url.readline()
    if not line_video_text:
        break
    if (e in line_video_text):
        f_video_text_hash.write(line_video_text)
        f_video_url_hash.write(line_video_url)

f_video_url.close()
f_video_text.close()