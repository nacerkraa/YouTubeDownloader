# importing the module
from pytube import YouTube

# where to save
SAVE_PATH = "home/nacer/project/python" #to_do

# link of the video to be downloaded
link = input("Enter your url: ")


yt = YouTube(link)

stream = yt.streams.first()

#to set the name of the file

# get the video with the extension and
# resolution passed in the get() function

try:
	# downloading the video
	stream.download(SAVE_PATH)

except:
	print("Some Error!")
print('Task Completed!')


