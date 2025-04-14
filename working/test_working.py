import pytest
from working import convert


def test_valid_conversions():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("8 PM to 8 AM") == "20:00 to 08:00"
    assert convert("8:00 PM to 8:00 AM") == "20:00 to 08:00"


def test_invalid_format():
    with pytest.raises(ValueError):
        convert("09:00 to 17:00")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("9AM to 5PM")
    with pytest.raises(ValueError):
        convert("10:7 AM - 5:1 PM")
    with pytest.raises(ValueError):
        convert("8:60 AM to 4:60 PM")


def test_out_of_range_times():
    with pytest.raises(ValueError):
        convert("13:00 AM to 1:00 PM")
    with pytest.raises(ValueError):
        convert("0:30 AM to 1:00 PM")
    with pytest.raises(ValueError):
        convert("9:61 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM to 5:60 PM")


def test_edge_cases():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"
    assert convert("1 AM to 1 PM") == "01:00 to 13:00"
    assert convert("11:59 AM to 11:59 PM") == "11:59 to 23:59"


def test_missing_to():
    with pytest.raises(ValueError):
        convert("9:00 AM 5:00 PM")
