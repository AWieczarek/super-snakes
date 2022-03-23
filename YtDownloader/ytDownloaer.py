import pytube

url = input("Dej linka do filma: ")

yt = pytube.YouTube(url)
video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
#video = yt.streams.get_highest_resolution()
print("Pobieram...")
print(video)
#video.download()
print("Pobralem!!!")
