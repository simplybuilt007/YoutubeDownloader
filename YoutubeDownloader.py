from pytube import YouTube

#res_itag_dict = {'360p': '18', '240p': '133', '144p': '160', '720p': '247'} #itag values according to respective resolutions

dlink = input("Enter the Youtube Video Link: ")
#res = input("Enter the resolution you want to download in(Ex: 144p,240p,360p,720p): ")

yt = YouTube(dlink)

#itag_val = int(res_itag_dict[res])#fetching itag from dictionary

dload = yt.streams.first()

dload.download("E:/DownloadTest")





