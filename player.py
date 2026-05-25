import subprocess
import yt_dlp
import os
import psutil
import sys

class Player:
    def __init__(self):
        self.process = None
        self.paused = False
        if sys.platform == "win32":
            self.mpv_path = os.path.join("bin", "mpv.exe")
        else:
            self.mpv_path = "mpv"

    def _get_audio_url(self, video_id: str) -> str:
        with yt_dlp.YoutubeDL({
            "format": "bestaudio",
            "quiet": True,
            "no_warnings": True,
            "noplaylist": True
        }) as ydl:
            info = ydl.extract_info(f"https://youtube.com/watch?v={video_id}", download=False)
            return info["url"]

    def play(self, video) -> None:
        self.stop()
        url = self._get_audio_url(video.video_id)

        if sys.platform == "win32":
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            startupinfo.wShowWindow = subprocess.SW_HIDE
            self.process = subprocess.Popen(
                [self.mpv_path, "--no-video", "--force-window=no", "--really-quiet", url],
                startupinfo=startupinfo,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                stdin=subprocess.DEVNULL
            )
        else:
            self.process = subprocess.Popen(
                [self.mpv_path, "--no-video", "--really-quiet", url],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                stdin=subprocess.DEVNULL
            )
        self.paused = False

    def pause(self) -> None:
        if self.process is None:
            return
        try:
            p = psutil.Process(self.process.pid)
            if not self.paused:
                p.suspend()
                self.paused = True
            else:
                p.resume()
                self.paused = False
        except psutil.NoSuchProcess:
            pass

    def stop(self) -> None:
        if self.process:
            try:
                p = psutil.Process(self.process.pid)
                if self.paused:
                    p.resume()
            except psutil.NoSuchProcess:
                pass
            self.process.kill()
            self.process = None
            self.paused = False

    def is_playing(self) -> bool:
        if self.process is None:
            return False
        return self.process.poll() is None