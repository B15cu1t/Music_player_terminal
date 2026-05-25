from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from api import VideoResult
import os
import sys

console = Console()

def init_terminal() -> None:
    if sys.platform == "win32":
        os.system('color')

class UI:
    def show_banner(self) -> None:
        banner = Text()
        banner.append("  ██████╗ ██╗   ██╗██████╗      ", style="bold color(208)")
        banner.append("╔══════════════════════════╗\n", style="dim color(208)")
        banner.append("  ██╔══██╗╚██╗ ██╔╝██╔══██╗     ", style="bold color(208)")
        banner.append("║  biscuit youtube player  ║\n", style="color(208)")
        banner.append("  ██████╔╝ ╚████╔╝ ██████╔╝     ", style="bold color(208)")
        banner.append("║  v1.0  by  Biscuit       ║\n", style="color(208)")
        banner.append("  ██╔══██╗  ╚██╔╝  ██╔═══╝      ", style="color(208)")
        banner.append("║  play music your way     ║\n", style="color(208)")
        banner.append("  ██████╔╝   ██║   ██║          ", style="color(208)")
        banner.append("╚══════════════════════════╝\n", style="dim color(208)")
        banner.append("  ╚═════╝    ╚═╝   ╚═╝\n", style="dim color(208)")
        console.print(banner)

    def show_results(self, results: list[VideoResult]) -> None:
        table = Table(title="Search Results", border_style="dim white", header_style="bold color(208)")
        table.add_column("#", style="color(208)", width=4)
        table.add_column("Title", style="white")
        table.add_column("Channel", style="dim white")
        table.add_column("Published", style="dim white")
        for i, video in enumerate(results, start=1):
            table.add_row(str(i), video.title, video.channel, video.published[:10])
        console.print(table)

    def show_queue(self, videos: list[VideoResult]) -> None:
        table = Table(title="Queue", border_style="dim white", header_style="bold color(208)")
        table.add_column("#", style="color(208)", width=4)
        table.add_column("Title", style="white")
        table.add_column("Channel", style="dim white")
        for i, video in enumerate(videos, start=1):
            table.add_row(str(i), video.title, video.channel)
        console.print(table)

    def show_now_playing(self, video: VideoResult, paused: bool = False) -> None:
        content = Text()
        content.append(video.title, style="bold white")
        content.append(f"\n{video.channel}", style="dim white")
        status = "[dim white]⏸  paused[/dim white]" if paused else "[color(208)]▶  now playing[/color(208)]"
        console.print(Panel(content, title=status, border_style="color(208)"))

    def get_input(self, prompt: str) -> str:
        if prompt != "/":
            console.print(f"[dim white]{prompt}[/dim white]")
        return console.input("[bold color(208)]> [/bold color(208)]").strip().lower()

    def clear(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')