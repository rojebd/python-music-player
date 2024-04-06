import random
import pytermgui as ptg
import just_playback
import pathlib
import threading
import time

try:
    from config import MUSIC_PATH
except ImportError:
    MUSIC_PATH = f"{__file__}"

try:
    from config import VOL_DOWN
except ImportError:
    VOL_DOWN = 3

try:
    from config import VOL_UP
except ImportError:
    VOL_UP = 3

try:
    from config import REWIND
except ImportError:
    REWIND = 3

try:
    from config import FORWARD
except ImportError:
    FORWARD = 3


current_volume = 0.5
playing = True
audio = just_playback.Playback()
songs_path = pathlib.Path(MUSIC_PATH)
total_songs = []
current_playing_song = None

try:
    for song in songs_path.iterdir():
        if str(song).endswith((".wav", ".mp3")):
            total_songs.append(song)

except FileNotFoundError:
    raise FileNotFoundError("Invalid directory or directory does not exist")


def load_song(song):
    global current_playing_song
    try:
        audio.stop()
        song = str(song)
        current_playing_song = str(pathlib.Path(song).name)
        audio.load_file(song)
        audio.play()

    except Exception as error:
        raise Exception(f"Invalid Audio File of type WAV or MP3 Error: {error}")

    return True


def toggle_audio():
    global playing
    if playing:
        audio.pause()
        playing = False
        return

    playing = True
    audio.resume()


def rewind(REWIND, multiplier):
    if multiplier > 0:
        current_position = audio.curr_pos
        audio.seek(current_position - REWIND * multiplier)
        return current_position - REWIND * multiplier

    current_position = audio.curr_pos
    audio.seek(current_position - REWIND)
    return current_position - REWIND


def forward(FORWARD, multiplier):
    if multiplier > 0:
        current_position = audio.curr_pos
        audio.seek(current_position + FORWARD * multiplier)
        return current_position + FORWARD * multiplier

    current_position = audio.curr_pos
    audio.seek(current_position + FORWARD)
    return current_position + FORWARD


def volume_up(VOL_UP, multiplier):
    global current_volume
    if multiplier > 0:
        current_volume += VOL_UP * multiplier
        audio.set_volume(current_volume)
        return current_volume + VOL_UP * multiplier

    current_volume += VOL_UP
    audio.set_volume(current_volume)
    return current_volume + VOL_UP


def volume_down(VOL_DOWN, multiplier):
    global current_volume
    if multiplier > 0:
        current_volume -= VOL_DOWN * multiplier
        audio.set_volume(current_volume)
        return current_volume - VOL_DOWN * multiplier

    current_volume -= VOL_DOWN
    audio.set_volume(current_volume)
    return current_volume - VOL_DOWN


current_song = ptg.Label(f"[app.text] ({current_playing_song})")
time_left = ptg.Label(f"[app.text] ({audio.curr_pos} / {audio.duration})")
volume = ptg.Label(f"[app.text] ( {audio.volume}%)")


def convert_seconds(seconds):
    minutes = str(seconds / 60)
    whole_minutes = minutes.split(".")
    whole_minutes = whole_minutes[0]

    diff = float(minutes) - float(whole_minutes)
    diff *= 60

    diff = int(diff)

    return f"{whole_minutes}:{diff}"


multiplier = 0
multiplier_button = ptg.Button(f"{multiplier}x", lambda *_: update_mult(5))


def update_mult(n):
    global multiplier
    multiplier += n


class MainControls(ptg.Container):
    def __init__(self):
        threading.Thread(target=self.update_widgets, daemon=True).start()
        super().__init__(
            ptg.Splitter(
                current_song,
                time_left,
                volume,
            ),
            "",
            ptg.Collapsible(
                "Songs",
                ptg.Container(
                    *[
                        ptg.Button(
                            str(song.name).replace(".wav", "").replace(".mp3", ""),
                            lambda _, song=song.absolute(): load_song(song),
                        )
                        for song in total_songs
                    ],
                ),
            ),
            "",
            ptg.Splitter(
                "",
                ptg.Button("", lambda *_: rewind(REWIND, multiplier)),
                ptg.Button(" ", lambda *_: toggle_audio()),
                ptg.Button("", lambda *_: forward(FORWARD, multiplier)),
                "",
                ptg.Button("󰝝", lambda *_: volume_up(VOL_UP, multiplier)),
                ptg.Button("󰝞", lambda *_: volume_down(VOL_DOWN, multiplier)),
                multiplier_button,
                "",
                "",
            ),
        )

    def update_widgets(self):
        global current_playing_song
        global multiplier
        while True:
            if multiplier > 15:
                multiplier = 0

            audio_curr_pos = convert_seconds(audio.curr_pos)
            audio_total = convert_seconds(audio.duration)
            multiplier_button.label = f"{multiplier}x"

            current_song.value = f"[app.text] ({current_playing_song})"
            time_left.value = f"[app.text] ({audio_curr_pos} / {audio_total})"
            volume.value = f"[app.text] ( {int(audio.volume * 100)}%)"

            if not audio.active and not playing:
                load_song(random.choice(total_songs))

            time.sleep(0.5)
