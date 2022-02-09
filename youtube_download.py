# Author: Adrian Patterson
# The following is a script that takes songs as arguments, retrieves a youtube link for each song, then downloads them to the users PC.

import urllib.request		# Necessary libraries
import re
from yt_dlp import YoutubeDL

print("\nEnter Youtube searches consecutively. Press 'enter' to begin downloads.\n")
query_list = []

while True:					# Loop to take in user requests for songs
	user_search = input("Song: ")

	if user_search == "":
		break
	
	user_search = user_search.replace(' ',"+")
	query_list.append(user_search)
		

for query in query_list:	# Loop to iterate over each song and download it to PC

	html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + query)	# Opens html for song search
	video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())  # Use of Regex findall to find and decode song IDs from youtube
	download_link = "https://www.youtube.com/watch?v=" + video_ids[0]	# Finally, the download link is ready
	print("https://www.youtube.com/watch?v=" + video_ids[0])

	ydl_opts = {			# Sets options for youtube downloader
		'format': 'bestaudio/best',
		'postprocessors': [{'key': 'FFmpegExtractAudio',
			            'preferredcodec': 'mp3',
			            'preferredquality': '192',}],
	       }

	with YoutubeDL(ydl_opts) as ydl:	# Downloads the song to the PC using youtube_dl
		ydl.download([download_link])