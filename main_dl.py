from pytube import Playlist
import youtube_downloader
import youtube_downloader_audio

from os import remove, mkdir
from shutil import rmtree, make_archive

try:
    remove("video.mp4")
except:
    pass
try:
    rmtree('./playlist')
    remove("playlist.zip")
except: 
    pass

BASE_YOUTUBE_URL = "https://youtu"
BASE_YOUTUBE_URL2 = "https://www.youtube.com"

BASE_PLAYLIST_URL = "https://youtube.com/playlist?list"
BASE_PLAYLIST_URL2 = "https://www.youtube.com/playlist?list"

def video_or_audio():
    print("Voulez vous telecharger une vidéo ou juste l'audio ?\n")

    print("1 - Vidéo")
    print("2 - Audio")

    choise = input("\nDonnez votre choix : ")

    while not choise == "1" and not choise == "2":
        choise = input("\nDonnez un nombre égale à 1 ou 2 : ")
    if choise == "1":
        return youtube_downloader
    elif choise == "2":
        return youtube_downloader_audio

def get_video_url_from_user():
    url = input("Donnez l'url d'une vidéo Youtube a telecharger:")
    url_lower = url.lower()
    if url_lower.startswith(BASE_YOUTUBE_URL) or url_lower.startswith(BASE_YOUTUBE_URL2):
        return url
    print("Ce lien n'est pas une url de vidéoyoutube")
    return get_video_url_from_user()

def get_playlist_url_from_user():
    url = input("Donnez l'url d'une playlist Youtube a telecharger:")
    url_lower = url.lower()
    if url_lower.startswith(BASE_PLAYLIST_URL) or url_lower.startswith(BASE_PLAYLIST_URL2):
        return url
    print("Ce lien n'est pas une url de playlist youtube")
    return get_playlist_url_from_user()

def dl_playlist_or_video():
    print("Voulez vous telecharger une seul vidéo ou toute une playlist ?\n")

    print("1 - Vidéo")
    print("2 - Playlist")

    choise = input("\nDonnez votre choix : ")
    while not choise == "1" and not choise == "2":
        choise = input("\nDonnez un nombre égale à 1 ou 2 : ")
    if choise == "1":
        url = get_video_url_from_user()
        YOUTUBE_DOWNLOADER.download_video(url)

    elif choise == "2":
        url = get_playlist_url_from_user()
        playlist_youtube = Playlist(url)
        print(f'Télecharement de la playlist {playlist_youtube.title}')
        mkdir("./playlist")
        for index, url in enumerate(playlist_youtube.video_urls):
            print(f"{index+1}/{len(playlist_youtube)}", end=" ")
            YOUTUBE_DOWNLOADER.download_video(url, 'playlist')
            make_archive('playlist', 'zip', 'playlist')

YOUTUBE_DOWNLOADER = video_or_audio()
dl_playlist_or_video()

input("\nTout a bien été téléchagé ")
