import urllib.request		
import re
import os
from yt_dlp import YoutubeDL

def get_user_queries() -> list[str]:
	print("\nEnter Youtube searches consecutively. Press 'enter' to begin downloads.\n")
	query_list = []

	while True:					
		user_search = input("Song: ")

		if user_search == "":
			break
		
		user_search = user_search.replace(' ',"+")
		query_list.append(user_search)
	
	return query_list
		

def download_queries(query_list: list[str]):
	if "Downloads" not in os.listdir():
		os.mkdir("Downloads")

	os.chdir("Downloads")
	
	for query in query_list:	
		html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + query)	
		video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())  
		download_link = "https://www.youtube.com/watch?v=" + video_ids[0]	
		print("Downloading https://www.youtube.com/watch?v=" + video_ids[0])

		ydl_opts = {			
			'format': 'bestaudio/best',
			'postprocessors': [{'key': 'FFmpegExtractAudio',
								'preferredcodec': 'mp3',
								'preferredquality': '192',}],
		}


		with YoutubeDL(ydl_opts) as ydl:	
			ydl.download([download_link])

if __name__ == '__main__':
	queries = get_user_queries()
	download_queries(queries)

