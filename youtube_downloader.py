from os import rename
from pytube import YouTube


def on_download_progress(stream, chunk, bytes_remaining):

	bytes_download = stream.filesize - bytes_remaining
	percent = bytes_download * 100 / stream.filesize
	print(f"Progression du téléchargement:{int(percent)}%")


def download_video(url, path=None):
	youtube_video = YouTube(url)
	youtube_video.register_on_progress_callback(on_download_progress)

	stream = youtube_video.streams.get_highest_resolution()

	print(f"Telechargment de {youtube_video.title}...")
	stream.download()

	filename = stream.default_filename
	if not path:
		rename(filename, "video.mp4")
	else:
		rename(filename, f"./{path}/{filename}")

	print("La vidéo à bien été téléchargé")
