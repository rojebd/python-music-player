from playbackcontrols import convert_seconds


def test_main():
    assert convert_seconds(108) == "1:48"
    assert convert_seconds(508) == "8:28"
    assert convert_seconds(203) == "3:23"
    assert convert_seconds(556) == "9:16"
