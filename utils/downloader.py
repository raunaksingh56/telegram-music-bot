import yt_dlp
import os

def download_song(query: str):
    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'outtmpl': '%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }]
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"ytsearch:{query}", download=True)['entries'][0]
            title = info.get('title')
            filename = ydl.prepare_filename(info).replace('.webm', '.mp3').replace('.m4a', '.mp3')
            return filename, title
    except Exception as e:
        print(f"[ERROR] {e}")
        return None, None
