import requests
import os
import json
import html
from dataclasses import dataclass


@dataclass
class VideoResult:
    title: str
    channel: str
    published: str
    video_id: str


class YouTubeAPI:
    def __init__(self):
        self.url = "https://www.googleapis.com/youtube/v3/search"
        self.key = self._load_key()

    def _load_key(self):
        key = os.getenv("YOUTUBE_API_KEY")
        if key:
            return key

        try:
            with open("config.json", "r") as f:
                data = json.load(f)
                return data.get("youtube_api_key")
        except (FileNotFoundError, json.JSONDecodeError):
            return None

    def is_ready(self):
        return bool(self.key)

    def search(self, query: str):
        if not self.key:
            return {"error": "NO_API_KEY"}

        try:
            params = {
                "part": "snippet",
                "q": query,
                "type": "video",
                "maxResults": 5,
                "key": self.key,
                "videoDuration": "any"
            }

            response = requests.get(self.url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()

            results = []

            for item in data.get("items", []):
                video_id = item.get("id", {}).get("videoId")
                if not video_id:
                    continue

                results.append(
                    VideoResult(
                        title=html.unescape(item["snippet"]["title"]),
                        channel=html.unescape(item["snippet"]["channelTitle"]),
                        published=item["snippet"]["publishedAt"],
                        video_id=video_id
                    )
                )

            return {"results": results}

        except requests.exceptions.RequestException:
            return {"error": "REQUEST_FAILED"}
