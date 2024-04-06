# Simple Python Music Player

[Description](#description)  
[Features](#features)  
[FAQ](#faq)  
[About](#about)  
[Configuration](#config)  
[Project Structure / Files](#project-files--structure)  
[Tests](#tests)  
[Depedencies / Running](#depedencies--running)  

### Screenshot:
![Alt text](./screenshot.png?raw=true "Screenshot of project")

### Description:
This is a simple TUI (Terminal User Interface) to play music files in python
made with the incredible TUI python library [pytermgui](https://github.com/bczsalba/pytermgui) and the audio
part is with the help of the simple and asynchronous audio library [just-playback](https://github.com/cheofusi/just_playback)

It has the ability to play most common audio files such as WAV and MP3
and has the ability to have some basic [configuration](#config)

It can also rewind, forward pause/play and some basic configuration

### Features:
  - Plays:
    - Wav Files
    - MP3 Files

  - Simple to use set the MUSIC_PATH Configuration variable to point to your music and 
    launch the app and start listening, If the varibable is not set then it sets it as the
    scripts directory

  - Forward by a multiplier 
  - Rewind by a multiplier
  - Volume Up by a multiplier
  - Volume Down by a multiplier
  - Shows current time left in the song (example 1:02 / 3:34 )


### About
This project is part of my CS50P Final project, I decided to make a simple TUI music
player because CMUS crashed when I switched to alpine linux


### Config

Configure the OPTIONS in the config.txt this file is at your home directory  
and is called .config.txt

All other options such as VOL_DOWN, VOL_UP, REWIND, FORWARD are optional and if not configured
are given a default value the value give is 3)

MUSIC_PATH if not configured is given the value of the playbackcontrols project __file__

For example a basic config file looks like this:

```text

  [Config]
  MUSIC_PATH = /home/roniell/coding/python/music-player/assets
  REWIND = 3
  FORWARD = 3
  VOL_UP = 3
  VOL_DOWN = 3

```


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
  pytest tests_project.py
  ```


# FAQ

Q: Can it play more files than just MP3 and WAV

A: No, other file formats are not implemented right now

Q: What does Exception: "Invalid Audio File of type WAV or MP3 Error" mean?

A: It means that the WAV or MP3 file you tried to play was not valid and the app could
   not play it

Q: What does FileNotFoundError "Invalid directory or directory does not exist"

A: It means that the directory specified in music path does not exist or is invalid
