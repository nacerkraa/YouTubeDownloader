# for download one video
# importing the module
from pytube import YouTube


# link of the video to be downloaded
link = input("Enter your url: ")

typeVideo = input("Type (y) for audio: ")

yt = YouTube(link)

if typeVideo == "y":
	stream = yt.streams.get_audio_only()
else:
	stream = yt.streams.get_highest_resolution()
try:
	stream.download("./path")
except:
	print("Some Error!")

print('Task Completed!')


