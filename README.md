# Simple Python Music Player

#### Video Demo: <URL Here>

#### Description:
This is a simple TUI (Terminal User Interface) to play music files in python
made with the incredible TUI python library [pytermgui] and the audio
part is with the help of the simple and asynchronous audio library [just-playback]

It has the ability to play most common audio files such as WAV and MP3
and has the ability to have some basic [configuration]

[configuration](#config)
[pytermgui]: https://github.com/bczsalba/pytermgui
[just-playback]: https://github.com/cheofusi/just_playback

##### Features:
  - Plays:
    - Wav Files
    - MP3 Files

  - Simple to use set the MUSIC_PATH Configuration variable to point to your music and 
    launch the app and start listening!

  - Forward and Rewind by a multiplier
  - Volume Up and Volume Down independtly of system volume by a multiplier
  - Shows time left in song (e.g 1:02 / 3:34 )


### About
This project is part of my CS50P Final project, I decided to make a simple TUI music
player because CMUS crashed when I switched to alpine linux


### Config

Configure the OPTIONS in the config.py this file must be at the root of the project
the only mandatory option to have configured so the program runs is MUSIC_PATH (the path to your music files)

All other options such as VOL_DOWN, VOL_UP, REWIND, FORWARD are optional and if not configured
are given a default value (the value being 3)

Options:

  - MUSIC_PATH:
    - MUST be an absolute path (/home/user/music instead of ~/music) to where your music has (directory can be empty)
    
  - REWIND:
    - How much to rewind by for example a rewind by and if set the multiplier how much to rewind by times the multiplier
  
  - FORWARD:
    - How much to forward by for example a forward by and if set the multiplier how much to forward by times the multiplier

  - VOL_DOWN:
    - By how much to turn the volume down

  - VOL_UP:
    - By how much to turn the volume up


