import json
import webbrowser
from rich.console import Console

console = Console()

CONFIG_FILE = "config.json"


def setup_api_key():
    console.print("\n[bold orange1]First Time Setup[/bold orange1]")
    console.print("[dim white]No YouTube API key found.[/dim white]\n")

    console.print("[white]Opening YouTube API page...[/white]")
    webbrowser.open(
        "https://console.cloud.google.com/apis/library/youtube.googleapis.com"
    )

    console.print("\n[bold white]Follow these steps:[/bold white]")
    console.print("[dim white]1.[/dim white] Sign into Google")
    console.print("[dim white]2.[/dim white] Create a project")
    console.print("[dim white]3.[/dim white] Enable YouTube Data API v3")
    console.print("[dim white]4.[/dim white] Create an API key")
    console.print("[dim white]5.[/dim white] Paste it below\n")

    api_key = input("Paste API key: ").strip()

    config = {
        "youtube_api_key": api_key
    }

    with open(CONFIG_FILE, "w") as file:
        json.dump(config, file, indent=4)

    console.print(
        "\n[bold green]Setup complete! Restart the app.[/bold green]"
    )


if __name__ == "__main__":
    setup_api_key()