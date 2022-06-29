def main():
    from pytube import YouTube

    yt = YouTube("https://www.youtube.com/watch?v=7BXJIjfJCsA")

    print(yt.title)

if __name__ == "__main__":
    main()

