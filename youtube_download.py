import urllib.request
import re
from youtube_dl import YoutubeDL

while True:
    user_search = input("Enter song:\t")

    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + user_search)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    download_link = "https://www.youtube.com/watch?v=" + video_ids[0]
    print("https://www.youtube.com/watch?v=" + video_ids[0])

    ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{'key': 'FFmpegExtractAudio',
                                    'preferredcodec': 'mp3',
                                    'preferredquality': '192',}],
               }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([download_link])