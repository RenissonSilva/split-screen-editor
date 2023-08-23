from pytube import YouTube
import numpy as np

def Download(link, theme):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download('downloads/'+theme)
    except:
        print("An error has occurred")

video_theme = ['barbixas', 'filmes', 'futebol', 'gaules', 'maromba']

for theme in video_theme:
    video_list = np.loadtxt('csv/'+theme+'.csv', delimiter=',', dtype=str)

    for link in video_list:
        Download(link, theme)