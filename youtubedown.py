from pytube import YouTube
url = "https://youtu.be/4p3gb7hct7Y?si=QeWk9PCaLLYJqcLZ"
yt = YouTube(url)
video_stream = yt.streams.get_highest_resolution()
video_stream.download()
print("complete download!")