from playbackcontrols import convert_seconds
from project import _define_layout
from project import _define_header
from project import _define_footer
import pytermgui as ptg


def test_playbackcontrols_conversion():
    assert convert_seconds(108) == "1:48"
    assert convert_seconds(508) == "8:28"
    assert convert_seconds(203) == "3:23"
    assert convert_seconds(556) == "9:16"


def test_define_layout():
    layout = _define_layout()
    assert str(layout.header.width) == "Auto(value=0)"
    layout.apply()
    assert len(layout.slots) == 5


def test_header_define():
    header = _define_header()
    assert header.width == 40
    assert header.height == 2
    assert header.is_persistent == False


def test_footer_define():
    manager = ptg.WindowManager()
    footer = _define_footer(manager)
    assert footer.width == 40
    assert footer.height == 2
    assert footer.is_persistent == False
