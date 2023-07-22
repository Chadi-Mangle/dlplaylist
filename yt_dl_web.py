from pytube import YouTube
from pytube import Playlist
import youtube_downloader
import youtube_downloader_audio

from os import remove, mkdir
from shutil import rmtree, make_archive

def video_or_audio(v_type):
	if v_type == "video":
		return youtube_downloader
	else:
		return youtube_downloader_audio


# def get_video_url_from_user():
# 	url = input("Donnez l'url d'une vidéo Youtube a telecharger:")
# 	url_lower = url.lower()
# 	if url_lower.startswith(BASE_YOUTUBE_URL) or url_lower.startswith(
# 	  BASE_YOUTUBE_URL2):
# 		return url
# 	print("Ce lien n'est pas une url de vidéoyoutube")
# 	return get_video_url_from_user()

# def get_playlist_url_from_user():
# 	url = input("Donnez l'url d'une playlist Youtube a telecharger:")
# 	url_lower = url.lower()
# 	if url_lower.startswith(BASE_PLAYLIST_URL) or url_lower.startswith(
# 	  BASE_PLAYLIST_URL2):
# 		return url
# 	print("Ce lien n'est pas une url de playlist youtube")
# 	return get_playlist_url_from_user()


def dl_playlist_or_video(downloader, link_type, url):
	try:
		remove("./video.mp4")
	except:
		pass
	try:
		remove("./video.mp3")
	except:
		pass
	try:
		rmtree('./playlist')
		remove("./playlist.zip")
	except:
		pass

	if link_type == "video":
		downloader.download_video(url)
		return f"{YouTube(url).streams.get_highest_resolution().default_filename}"
	else:
		playlist_youtube = Playlist(url)
		# print(f'Télecharement de la playlist {playlist_youtube.title}')
		mkdir("./playlist")
		for index, url in enumerate(playlist_youtube.video_urls):
			# print(f"{index+1}/{len(playlist_youtube)}", end=" ")
			downloader.download_video(url, 'playlist')

		make_archive('playlist', 'zip', 'playlist')
		return f"{playlist_youtube.title.replace(' ', '_')}.zip"


def get_playlist_or_video_info(link_type, url):
	if link_type == 'video':
		video = YouTube(url)
		title = video.title
		thumbnail = video.thumbnail_url
	else:
		playlist = Playlist(url)
		title = playlist.title
		thumbnail = playlist.videos[0].thumbnail_url

	return title, thumbnail


# get_playlist_or_video_info(
#  'playlist',
#  'https://www.youtube.com/playlist?list=PLzFEhfPxC4TqSPhIbp5lmqvzZ1lzGi5wE')
