# Tkinter Music Player

A personal desktop-application project that brings local audio playback into a simple graphical interface. It explores how a playlist, playback state, sliders, and background progress updates can work together in an event-driven Python application.

## Main capabilities

- Load a local directory into a playlist and select a track.
- Play, pause, and resume audio.
- Move between tracks with previous/next controls.
- Switch between normal playback progression and replay mode.
- Adjust volume and seek through the current track.

## Design and technologies

The application separates its interface, playback coordination, and audio operations. Tkinter provides the window and controls, while Pygame's mixer performs playback. A background thread tracks the playback position so the interface can display progress.

| File | Responsibility |
| --- | --- |
| [MusicPlayer.py](MusicPlayer.py) | Playlist actions, playback state, and progress tracking |
| [MusicTool.py](MusicTool.py) | Wrapper around Pygame audio operations |
| [UI.py](UI.py) | Tkinter layout and controls |

## Personal record

This repository documents an early exercise in GUI design, event handling, threading, and separating application responsibilities. It is a local-file player, with no streaming service or online music catalog. Audio files are not included, and the directory listing does not filter out non-audio entries; playback behavior depends on the file format and audio backend.
