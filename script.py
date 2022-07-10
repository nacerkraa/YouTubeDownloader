#import the package
from pprint import pp
from pytube3 import YouTube

url = 'https://www.youtube.com/watch?v=7BXJIjfJCsA'
my_video = YouTube(url)

print(my_video.title)


