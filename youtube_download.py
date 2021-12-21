# Author: Adrian Patterson
# The following is a script that takes songs as arguments, retrieves a youtube link for each song, then downloads them to the users PC.

import urllib.request		# Necessary libraries
import re
import os
from moviepy.editor import *
from pytube import YouTube

print("\nEnter youtube searches consecutively. Enter 'done' to begin downloads.\n\n")
query_list = []

while True:					# Loop to take in user requests for songs
    user_search = input("Enter song:\t")

    if user_search == "done":
        break

    user_search = user_search.replace(' ', "+")
    query_list.append(user_search)


for query in query_list:  # Loop to iterate over each song and download it to PC

    # Opens html for song search
    html = urllib.request.urlopen(
        "https://www.youtube.com/results?search_query=" + query)
    # Use of Regex findall to find and decode song IDs from youtube
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    download_link = "https://www.youtube.com/watch?v=" + \
        video_ids[0]  # Finally, the download link is ready
    print("Downloading from " +
          "https://www.youtube.com/watch?v=" + video_ids[0])

    youtube = YouTube(download_link)
    youtube.streams.filter(progressive=True, file_extension='mp4').order_by(
        'resolution').desc().first().download()

for file in os.listdir(os.getcwd()):
    file_name, file_type = os.path.splitext(file)
    if file_type == ".mp4":
        video_file = VideoFileClip(file)
        audio_file = video_file.audio
        audio_file.write_audiofile(file_name + ".mp3")
        os.remove(file)
