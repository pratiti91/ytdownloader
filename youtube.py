from pytube import YouTube
yt=YouTube("https://www.youtube.com/watch?v=ZfSPZmtXaEc&ab_channel=Mariners%27BaseCampTV")

x=yt.streams.filter(file_extension="mp4")
y=x.get_by_resolution("360p")
y.download("d:/qrcode")