import yt_dlp

def musicLink(IdMusic):

    ydl_opts = {
        'format': 'best',
        'quiet': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info((f"https://www.youtube.com/watch?v={IdMusic}"), download=False)
        return info["url"]
