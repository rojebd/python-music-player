import pytermgui as ptg
import just_playback
import pathlib
import threading
import time

try:
    from config import MUSIC_PATH
except ImportError:
    raise ImportError("Must have MUSIC_PATH declared")


current_volume = 0.5
PLAYING = True
audio = just_playback.Playback()
songs_path = pathlib.Path(MUSIC_PATH)
total_songs = []
current_playing_song = None

for song in songs_path.iterdir():
    if str(song).endswith((".wav", ".mp3")):
        total_songs.append(song)


def load_song(song):
    global current_playing_song
    audio.stop()
    song = str(song)
    current_playing_song = str(pathlib.Path(song).name)
    audio.load_file(song)
    audio.play()


def toggle_audio():
    global PLAYING
    if PLAYING:
        audio.pause()
        PLAYING = False
        return

    PLAYING = True
    audio.resume()


def rewind():
    current_position = audio.curr_pos
    audio.seek(current_position - 10)


def forward():
    current_position = audio.curr_pos
    audio.seek(current_position + 10)


def volume_up():
    global current_volume
    current_volume += 0.1
    audio.set_volume(current_volume)


def volume_down():
    global current_volume
    current_volume -= 0.1
    audio.set_volume(current_volume)


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
            ptg.Splitter(
                "",
                ptg.Button("", lambda *_: rewind()),
                ptg.Button(" ", lambda *_: toggle_audio()),
                ptg.Button("", lambda *_: forward()),
                "",
                ptg.Button("󰝝", lambda *_: volume_up()),
                ptg.Button("󰝞", lambda *_: volume_down()),
                "",
                "",
            ),
        )

    def update_widgets(self):
        global current_playing_song
        while True:
            audio_curr_pos = convert_seconds(audio.curr_pos)
            audio_total = convert_seconds(audio.duration)

            current_song.value = f"[app.text] ({current_playing_song})"
            time_left.value = f"[app.text] ({audio_curr_pos} / {audio_total})"
            volume.value = f"[app.text] ( {int(audio.volume * 100)}%)"

            time.sleep(1.5)
