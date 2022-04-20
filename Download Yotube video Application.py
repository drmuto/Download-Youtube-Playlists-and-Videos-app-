from pytube import YouTube
Vidz = input('Please enter Your Youtube video link:')
yt= YouTube(Vidz)
quality_of_video = int(input('please type the resolution: 360,720,1080(not available now):---'))
if quality_of_video == 360:
    yt.streams.filter(file_extension='mp4',resolution="360p")
    stream= yt.streams.get_by_itag(18)
    print('your download is starting in 360p and will be stored wherever this program is stored')
    stream.download()
    
if quality_of_video == 720:
    yt.streams.filter(file_extension='mp4',resolution="720p")
    stream= yt.streams.get_by_itag(22)
    stream.download()
    print('your download is starting in 720p and will be stored wherever this program is stored')
    

#[<Stream: itag="18" mime_type="video/mp4" res="360p" fps="30fps" vcodec="avc1.42001E" acodec="mp4a.40.2" progressive="True" type="video">,
#<Stream: itag="22" mime_type="video/mp4" res="720p" fps="30fps" vcodec="avc1.64001F" acodec="mp4a.40.2" progressive="True" type="video">,
#<Stream: itag="137" mime_type="video/mp4" res="1080p" fps="30fps" vcodec="avc1.640028" progressive="False" type="video">,
    

             
