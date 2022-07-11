# importing the module
from pytube import YouTube


# link of the video to be downloaded
link = input("Enter your url: ")


yt = YouTube(link)

stream = yt.streams.get_audio_only()
# stream = yt.streams.get_highest_resolution()

try:
	stream.download("Home/Downloads")
except:
	print("Some Error!")
print('Task Completed!')


