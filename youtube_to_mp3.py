import urllib.request
import re
import os
import argparse
from yt_dlp import YoutubeDL
from concurrent.futures import ThreadPoolExecutor

def get_user_queries() -> list[str]:
	print("\nEnter Youtube searches consecutively. Press 'enter' with an empty search to begin downloads.\n")
	query_list = []

	while True:					
		user_search = input("Song: ")

		if user_search == "":
			break
		
		user_search = user_search.replace(' ', "+")
		query_list.append(user_search)
	
	return query_list

def download_video(query: str, download_dir: str):
	html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + query)	
	video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
	download_link = "https://www.youtube.com/watch?v=" + video_ids[0]
	print(f"Downloading {download_link}")

	ydl_opts = {			
		'format': 'bestaudio/best',
		'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),  
		'postprocessors': [{
			'key': 'FFmpegExtractAudio',
			'preferredcodec': 'mp3',
			'preferredquality': '192',
		}],
	}

	with YoutubeDL(ydl_opts) as ydl:	
		ydl.download([download_link])

def download_queries(query_list: list[str], download_dir: str):
	if not os.path.exists(download_dir):
		os.makedirs(download_dir)

	with ThreadPoolExecutor() as executor:
		executor.map(lambda query: download_video(query, download_dir), query_list)

def parse_args():
	parser = argparse.ArgumentParser(description="Download YouTube audio as MP3.")
	parser.add_argument(
		'-d', '--directory', type=str, default='Downloads', help="Directory to save downloaded MP3 files"
	)
	return parser.parse_args()

if __name__ == '__main__':
	args = parse_args()
	queries = get_user_queries()
	download_queries(queries, args.directory)
