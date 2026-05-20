import yt_dlp

mus = {
    'format': 'bestaudio/best',
    'outtmpl': 'downloads/song.mp3',
    'quiet': True
}

def download_music(url):

    with yt_dlp.YoutubeDL(mus) as ydl:
        ydl.download([url])

    return 'downloads/song.mp3'