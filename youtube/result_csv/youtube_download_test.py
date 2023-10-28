from os import listdir, rename, scandir, remove
from os.path import isdir, isfile, splitext
from shutil import copy2
from yt_dlp import YoutubeDL
from time import time


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)

def my_hook(d):
    if d["status"] == "finished":
        print("Done downloading, now converting ...")


def YouTubeDownload(
    addr,
    filepath
):
    # 유튜브 주소 기반 다운로드
            download_list = [addr, ]
            ydl_opt = {
                'format': 'best[height<=720]',
                'outtmpl': filepath,
                'postprocessors': [
                    {
                        'key': 'FFmpegVideoConvertor',
                        'preferedformat': 'mp4',
                        # 'preferedquality': '1',
                    },
                    {
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'none',  # 음성 제거
                    }
                ],

                "logger": MyLogger(),
                'progress_hooks': [my_hook],
                'cachedir': False,
                'noplaylist': True,
                "cookiefile":  "cookies.txt",
            }

            for z in range(5):
                try:
                    with YoutubeDL(ydl_opt) as ydl:
                        ydl.download(download_list)
                    break
                except Exception as e:
                    print(f"Over ERROR {z} in Youbube_dl ({e})")
                    if z >= 4:
                        return

YouTubeDownload(
    addr="https://www.youtube.com/watch?v=CEOrj9Y9fLk",
    filepath="test"
)