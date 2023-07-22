from os import rename
from pytube import YouTube


def on_download_progress(stream, chunk, bytes_remaining):

	bytes_download = stream.filesize - bytes_remaining
	percent = bytes_download * 100 / stream.filesize
	print(f"Progression du téléchargement:{int(percent)}%")


def download_video(url, path=None):

	youtube_video = YouTube(url)
	youtube_video.register_on_progress_callback(on_download_progress)

	streams = youtube_video.streams.filter(
	 progressive=False,
	 file_extension='mp4',
	 type='audio',
	).order_by('abr').desc()
	audio_stream = streams[0]

	print(f"Telechargment de {youtube_video.title}...")

	audio_stream.download()

	filename = audio_stream.default_filename
	if not path:
		rename(filename, "video.mp4")
	else:
		rename(filename, f"./{path}/{filename[:-1]+'3'}")
	print("L'audio à bien été téléchargé")
