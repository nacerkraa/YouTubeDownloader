# importing the module
from pytube import YouTube

# where to save
SAVE_PATH = "home/nacer/project/python" #to_do

# link of the video to be downloaded
link = input("Enter your url: ")


yt = YouTube(link)

stream = yt.streams.first()

try:
	stream.download(SAVE_PATH)
except:
	print("Some Error!")
print('Task Completed!')


