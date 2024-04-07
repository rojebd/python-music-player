import pytermgui as ptg
from playbackcontrols import MainControls, audio, toggle_audio
from palette_colors import *


def _confirm_exit(manager, audio):
    def stop_music_handle_exit():
        audio.stop()
        manager.stop()

    exit_window = ptg.Window(
        "[app.text] Are you sure you want to quit?",
        "",
        ptg.Container(
            ptg.Splitter(
                ptg.Button("Yes", lambda *_: stop_music_handle_exit()),
                ptg.Button("No", lambda *_: exit_window.close()),
            ),
        ),
    ).center()

    exit_window.select(1)
    manager.add(exit_window)


def _define_aliases():
    ptg.tim.alias("app.text", f"{FOREGROUND}")
    # ptg.tim.alias("app.header", f"bold @{GREEN} {FOREGROUND}")  # bold BG_COLOR FG_COLOR
    # ptg.tim.alias("app.header.fill", f"@{GREEN}")  # BG_COLOR

    ptg.tim.alias(
        "app.header", f"italic @{LIGHT_BLUE} {BACKGROUND}"
    )  # bold BG_COLOR FG_COLOR
    ptg.tim.alias("app.header.fill", f"@{LIGHT_BLUE}")  # BG_COLOR

    ptg.tim.alias("app.button.label", f"bold @{BLUE} app.text")
    ptg.tim.alias("app.button.highlight", f"bold @{LIGHT_RED} app.text")

    ptg.tim.alias("app.footer", f"bold @{GREEN} {FOREGROUND}")
    ptg.tim.alias("app.footer.fill", f"@{GREEN}")

    ptg.tim.alias("app.sidebar", f"bold @{GREEN} {FOREGROUND}")
    ptg.tim.alias("app.sidebar.fill", f"@{GREEN}")

    ptg.tim.alias("app.controls", f"bold @{GREEN} {FOREGROUND}")
    ptg.tim.alias("app.controls.fill", f"@{GREEN}")


def _define_layout():
    layout = ptg.Layout()
    layout.add_slot("Header", height=1)
    layout.add_break()
    layout.add_slot("Controls")
    layout.add_break()
    layout.add_slot("Footer", height=3)

    return layout


def _config_widgets():
    ptg.boxes.DOUBLE.set_chars_of(ptg.Window)
    ptg.boxes.ROUNDED.set_chars_of(ptg.Container)
    ptg.Button.styles.label = "app.button.label"
    ptg.Button.styles.highlight = "app.button.highlight"
    ptg.Slider.styles.filled__cursor = BLUE
    ptg.Slider.styles.filled_selected = LIGHT_BLUE
    ptg.Label.styles.value = "app.text"
    ptg.Window.styles.border__corner = LIGHT_BLUE
    ptg.Container.styles.border__corner = LIGHT_GRAY
    ptg.Splitter.set_char("separator", "")


def _define_header():
    header = ptg.Window(
        "[app.header] Simple Python Music Player", box="EMPTY", is_persistant=True
    )
    header.styles.fill = "app.header.fill"

    return header


def _define_footer(manager):
    footer = ptg.Window(
        ptg.Button("[app.text] Exit", lambda *_: _confirm_exit(manager, audio)),
        box="EMPTY",
    )

    return footer


def main():
    with ptg.WindowManager() as manager:
        _define_aliases()
        _config_widgets()
        manager.layout = _define_layout()
        header = _define_header()

        controls = ptg.Window(
            MainControls(),
            box="EMPTY",
        )

        footer = _define_footer(manager)

        manager.add(header)
        manager.add(controls)
        manager.add(footer)

        manager.bind(ptg.keys.SPACE, toggle_audio)


if __name__ == "__main__":
    main()
