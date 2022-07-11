# for download playlist
from pytube import Playlist
p = Playlist('https://www.youtube.com/playlist?list=PLzMcBGfZo4-kCLWnGmK0jUBmGLaJxvi4j')

print(f'Downloading: {p.title}')
i = 0;
for video in p.videos:
    i += 1
    print(video.title)
    if i >= 10:
        st = video.streams.get_highest_resolution()
        st.download()
    #video.streams.first().download()