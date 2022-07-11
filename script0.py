from pytube import Playlist
p = Playlist('https://www.youtube.com/playlist?list=PLGo0NLnuNoa-KKJPn8ZBRjksb8jaw4lz-')

print(f'Downloading: {p.title}')

for video in p.videos:
    print(video.title)
    st = video.streams.get_highest_resolution()
    st.download()
    #video.streams.first().download()