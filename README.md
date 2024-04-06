# Simple Python Music Player

### Video Demo: <URL Here>

### Screenshot:
![Alt text](./screenshot.png?raw=true "Screenshot of project")

### Description:
This is a simple TUI (Terminal User Interface) to play music files in python
made with the incredible TUI python library [pytermgui](https://github.com/bczsalba/pytermgui) and the audio
part is with the help of the simple and asynchronous audio library [just-playback](https://github.com/cheofusi/just_playback)

It has the ability to play most common audio files such as WAV and MP3
and has the ability to have some basic [configuration](#config)


### Features:
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


### Project Files / Structure

  project.py:
    - Main File where layout for the TUI is defined and window is started

  playbackcontrols.py:
    - Where the logic for the TUI is for example loading songs, updating TUI widgets

  palette_colors.py:
    - Where some global variables for the TUI colors are initialized, they are put in a separate file to not bloat the main file

  config.py:
    - Your configuration file for the TUI to configure it see [configuration](#config)

### Depedencies / Running
The depedencies are in the in the requirements.txt
to run install and run the project:

  ```shell

    git clone https://github.com/rojebd/python-music-player
    cd python-music-player
    pip install -r requirements.txt
    python project.py
  
  ```


### Tests

The tests are run using [Pytest](https://docs.pytest.org/en/8.0.x/)

to run the tests:

  ```shell
    pytest tests/
  ```
