import pytermgui as ptg
from playbackcontrols import MainControls
from boilerplate_setup import (
    _define_aliases,
    _define_footer,
    _define_layout,
    _config_widgets,
    _define_header,
)

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
