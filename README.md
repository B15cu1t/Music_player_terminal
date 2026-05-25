# Biscuit YouTube Player  
**Terminal-Based Audio Streamer & Process Manager**

---

## Overview
This project is a **command-line YouTube music player** implemented purely in **Python**.  
It demonstrates the integration of **third-party REST APIs**, **cross-platform OS process management**, and **dynamic terminal UI design** to create a seamless music listening experience directly from the terminal.

The system allows users to search YouTube, queue audio streams, and control playback asynchronously while keeping the terminal interface responsive.

---

## Architecture & Workflow
The project is built using an object-oriented architecture separated into distinct modules:

- **API Module (api.py):** Handles communication with the YouTube Data API v3 to fetch search results and parse JSON metadata.
- **Player Module (player.py):** Uses yt-dlp to extract direct audio stream URLs, bypassing video overhead. It spawns a headless mpv background process to play the audio.
- **Queue Manager (music_queue.py):** Maintains the data structure for upcoming tracks.
- **UI & State Manager (main.py & ui.py):** Drives the interactive application loop, rendering terminal graphics using the rich library and capturing user input without interrupting playback.

---

## Advanced Process Handling
A core technical focus of this project is the management of the external media player (mpv):
- **Cross-Platform Execution:** Dynamically adjusts execution paths depending on whether the host is Windows (win32) or Unix-based.
- **Hidden Subprocesses:** On Windows, it manipulates subprocess.STARTUPINFO flags to completely hide the mpv console window, ensuring a true background process.
- **State Manipulation:** Instead of killing and restarting streams, the application uses psutil to send OS-level suspend and resume signals to the PID, enabling instant pause/play functionality.

---

## Features
- Live Search via YouTube Data API v3 integration  
- Headless streaming using high-quality audio formats  
- OS-level process suspension for instantaneous playback control  
- Dynamic queueing for multiple tracks  
- Stylized, color-coded terminal UI  
- Automated configuration script for API key generation  

---

## Technologies Used
- **Python 3**
- **yt-dlp** – Advanced media stream extraction
- **psutil** – Cross-platform system and process utility manipulation
- **subprocess** – Low-level OS process spawning and I/O redirection
- **requests** – HTTP/REST API communication
- **rich** – Advanced terminal formatting and UI components
- **mpv** – Command-line media player backend

---

## Educational Goals
Through this project, I gained practical experience with:
- Managing and interacting with child processes in a cross-platform environment
- Utilizing OS-level signals for application state control
- Consuming and parsing structured data from external REST APIs
- Building responsive, state-driven CLI applications
- Managing project dependencies and separating binaries from source code

This project strengthened my understanding of **how high-level applications interact with low-level operating system resources**.

---

## Installation & Setup
For detailed installation instructions regarding Python dependencies and setting up the mpv backend for your specific operating system (Windows, Linux, or macOS), please refer to the included INSTALL.txt guide.

---

## Limitations
- Playback queue does not auto-advance; it requires user input to skip to the next track
- Relies on personal Google Cloud API quotas for search queries
- Playback relies entirely on the external mpv binary being properly installed

---

## Future Improvements
Possible enhancements include:
- Asynchronous threading to monitor the mpv process state and auto-advance the queue
- Support for extracting and queuing entire YouTube playlists
- Local caching for search results to minimize API calls
- IPC (Inter-Process Communication) with mpv to control volume directly from the terminal

---

## Ethical Disclaimer
**This project is strictly a front-end interface built for educational purposes.**

- It does not bypass DRM (Digital Rights Management)  
- It relies entirely on publicly available APIs and open-source extraction tools  
- Users are responsible for adhering to YouTube's Terms of Service regarding media streaming  

---

## Relevance
Building CLI-based wrappers for complex tasks is a foundational skill in:
- System Administration
- Tool Development
- Lightweight Application Design
- API Integration
