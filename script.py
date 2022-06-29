def main():
    # importing the module
    from pytube import YouTube

    yt = YouTube("https://www.youtube.com/watch?v=NtzDjNhPZgU")

    print(yt)

if __name__ == "__main__":
    main()

