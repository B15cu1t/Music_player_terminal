from api import VideoResult

class Queue:
    def __init__(self):
        self.videos = []

    def add(self, video: VideoResult):
        self.videos.append(video)

    def remove(self, index: int):
        self.videos.pop(index)

    def clear(self):
        self.videos.clear()

    
    def next(self) -> VideoResult:
        return self.videos.pop(0)
    

    def is_empty(self) -> bool:
        return len(self.videos) == 0

        


