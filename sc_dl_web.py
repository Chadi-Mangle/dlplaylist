import youtube_dl
import requests
from bs4 import BeautifulSoup

from os import remove, mkdir
from shutil import rmtree, make_archive

def dl_playlist_or_video(url):
	try:
		remove("./video.mp3")
	except:
			pass
	try:
		rmtree('./playlist')
		remove("./playlist.zip")
	except:
		pass

	if '/sets/' in url:
		ydl_opts = {
		 'outtmpl': './playlist/%(title)s.%(ext)s',
		 'extract_flat ': 'in_playlist'
		}
	else:
		ydl_opts = {'outtmpl': './video.mp3'}

	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		data = ydl.extract_info(url, download=False)
		ydl.download([url])

	if '/sets/' in url:
			make_archive('playlist', 'zip', 'playlist')
			return data['title'] + '.zip' 
	return {data['title']} + '.mp3'


def get_playlist_or_video_info(url):
	response = requests.get(url)
	if response.status_code == 200:
		soup = BeautifulSoup(response.content, 'html.parser')
		title = soup.find('meta', property='og:title')['content']
		cover_url = soup.find('meta', property='og:image')['content']
		return title, cover_url
		