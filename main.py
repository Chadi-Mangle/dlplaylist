from flask import Flask, render_template, request, redirect, url_for, send_file
import yt_dl_web
import sc_dl_web
import youtube_downloader
import youtube_downloader_audio

BASE_YOUTUBE_URL = "https://youtu.be"
BASE_YOUTUBE_URL2 = "https://www.youtube.com"

BASE_PLAYLIST_URL = "https://youtube.com/playlist?list"
BASE_PLAYLIST_URL2 = "https://www.youtube.com/playlist?list"

BASE_SOUNDCLOUD_URL = "https://soundcloud.com/"


app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def index():
	if request.method == "POST":
		platform = request.form['platform']
		video_type = request.form['video_type']
		link_type = request.form['link_type']
		print(platform)
		if platform == "yt":
			if link_type == "video":
				url_type1 = BASE_YOUTUBE_URL
				url_type2 = BASE_YOUTUBE_URL2
			else:
				url_type1 = BASE_PLAYLIST_URL
				url_type2 = BASE_PLAYLIST_URL2

			return render_template("get_yt_url.html",
								platform=platform,
								link_type=link_type,
								video_type=video_type,
								url_type1=url_type1,
								url_type2=url_type2)
		elif platform == "sc":
			url_type1 = BASE_SOUNDCLOUD_URL

			return render_template("get_sc_url.html",
								platform=platform,
								link_type=link_type,
								video_type=video_type,
								url_type1=url_type1)


	return render_template("index.html")


@app.route('/link', methods=["POST", "GET"])
def link():
	if request.method == "POST":
		platform = request.args.get('platform')
		video_type = request.args.get('video_type')
		link_type = request.args.get('link_type')
		url = request.form['url']

		if platform == 'yt':
			title, thumbnail = yt_dl_web.get_playlist_or_video_info(link_type, url)
			return render_template("download_page.html",
								platform=platform,
								link_type=link_type,
								video_type=video_type,
								url=url,
								title=title,
								thumbnail=thumbnail)
		elif platform == 'sc':
			title, thumbnail = sc_dl_web.get_playlist_or_video_info(url)
			return render_template("download_page.html",
								platform=platform,
								link_type=link_type,
								video_type=video_type,
								url=url,
								title=title,
								thumbnail=thumbnail)


@app.route("/download", methods=["POST", "GET"])
def download():
	platform = request.args.get('platform')
	video_type = request.args.get('video_type')
	link_type = request.args.get('link_type')
	url = request.args.get('url')

	if platform == 'yt':
		downloader = yt_dl_web.video_or_audio(video_type)
		filename = yt_dl_web.dl_playlist_or_video(downloader, link_type, url)

		if link_type == "video":
			if video_type == "video":
				return send_file("./video.mp4",
								as_attachment=True,
								download_name=filename)
			else:
				return send_file("./video.mp4",
								as_attachment=True,
								download_name=filename[:-1]+'3')
				
	elif platform == 'sc':
		filename = sc_dl_web.dl_playlist_or_video(url)
		if link_type == "video":
			return send_file("./video.mp3",
							as_attachment=True,
							download_name=filename)
			
	return send_file("./playlist.zip",
							as_attachment=True,
							download_name=filename)


app.run(host='0.0.0.0', port=81, debug=True)
# app.run(host='0.0.0.0', port=81)