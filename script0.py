# for download playlist
from pytube import Playlist

url = input('paste the url: ')

p = Playlist(url)

print(f'Downloading: {p.title}')

for video in p.videos:

    print(video.title)
    st = video.streams.get_highest_resolution()
    st.download()
    # video.streams.first().download()