from api import YouTubeAPI
from music_queue import Queue
from player import Player
from ui import UI, console, init_terminal
import subprocess
import sys

class App:
    def __init__(self):
        self.api = YouTubeAPI()
        self.queue = Queue()
        self.player = Player()
        self.ui = UI()
        self.current_video = None

    def run(self):
        while True:
            self.ui.clear()
            self.ui.show_banner()

            if self.current_video and not self.player.is_playing() and not self.player.paused:
                if not self.queue.is_empty():
                    video = self.queue.next()
                    console.print("[dim white]  fetching stream...[/dim white]")
                    self.player.play(video)
                    self.current_video = video
                else:
                    self.current_video = None

            if self.current_video:
                self.ui.show_now_playing(self.current_video, self.player.paused)

            console.print("[dim orange1]  search  play  pause  queue  skip  stop  quit[/dim orange1]\n")
            command = self.ui.get_input("/")

            if command == "search":
                self.ui.clear()
                self.ui.show_banner()
                query = self.ui.get_input("Search query:")
                results_data = self.api.search(query)

                if "error" in results_data:
                    if results_data["error"] == "NO_API_KEY":
                        self.ui.get_input("No API key found. Starting setup... Press enter.")
                        subprocess.run([sys.executable, "setup.py"])
                        self.ui.get_input("Setup complete. Restarting required. Press enter to exit.")
                        self.player.stop()
                        exit()
                    else:
                        self.ui.get_input("Network error. Try again. Press enter.")
                        continue

                results = results_data["results"]

                if not results:
                    self.ui.get_input("No results found. Press enter.")
                    continue

                self.ui.show_results(results)
                choice_input = self.ui.get_input("Add to queue (or press enter to cancel):")

                if choice_input == "":
                    continue

                if not choice_input.isdigit():
                    self.ui.get_input("Invalid input. Press enter to continue.")
                    continue

                choice = int(choice_input)

                if choice < 1 or choice > len(results):
                    self.ui.get_input("Invalid selection. Press enter to continue.")
                    continue

                self.queue.add(results[choice - 1])

            elif command == "play":
                if self.queue.is_empty():
                    self.ui.get_input("Queue is empty! Press enter to continue.")
                else:
                    video = self.queue.next()
                    console.print("[dim white]  fetching stream...[/dim white]")
                    self.player.play(video)
                    self.current_video = video

            elif command == "queue":
                self.ui.clear()
                self.ui.show_banner()
                self.ui.show_queue(self.queue.videos)
                self.ui.get_input("Press enter to continue...")

            elif command == "skip":
                self.player.stop()
                if not self.queue.is_empty():
                    video = self.queue.next()
                    console.print("[dim white]  fetching stream...[/dim white]")
                    self.player.play(video)
                    self.current_video = video
                else:
                    self.current_video = None

            elif command == "stop":
                self.player.stop()
                self.current_video = None

            elif command == "pause":
                self.player.pause()

            elif command == "quit":
                self.player.stop()
                exit()

init_terminal()
app = App()
app.run()
