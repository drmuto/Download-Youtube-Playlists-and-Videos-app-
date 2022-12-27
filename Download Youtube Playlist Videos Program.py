from pytube import Playlist
p= input("enter Your Youtube Playlist Link:----")
m = Playlist(p)
print(f'Downloading: {m.title}')
#we are running a "for" loop in our Youtube PLaylist so that we can iterate through each of the video
for video in m.videos:
    #video.streams.first().download() this one is for lowest quality possible
    #video.streams.get_highest_resolution().download() this one is for highest quality possible not recommened because you might end up with 1080 video with no audio
    #remember pytube only offers 720p as the highest video resolution if you want to download 1080p you have to download audioa and video separately
    
    #this one is for downloading at custom video quality
    video.streams.get_highest_resolution().download()
    print('your playlist is being downloaded be patient')  
