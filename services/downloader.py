import os
import re
import uuid

import yt_dlp

from config import DOWNLOAD_DIR


def is_supported_url(text: str) -> bool:
    return bool(re.match(r"https?://", text))


def download_music(url: str) -> str | None:
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)

    file_id = uuid.uuid4().hex
    opts = {
        "format": "bestaudio/best",
        "outtmpl": os.path.join(DOWNLOAD_DIR, file_id + ".%(ext)s"),
        "quiet": True,
    }

    try:
        with yt_dlp.YoutubeDL(opts) as ydl:
            ydl.download([url])
    except Exception:
        return None

    for fname in os.listdir(DOWNLOAD_DIR):
        if fname.startswith(file_id):
            return os.path.join(DOWNLOAD_DIR, fname)

    return None
