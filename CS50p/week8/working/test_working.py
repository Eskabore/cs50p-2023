import pytest
from working import convert

def test_valid_pattern_1():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

def test_valid_pattern_2():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_valid_midnight():
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"

def test_valid_leading_zeros():
    assert convert("7:00 PM to 4:05 AM") == "19:00 to 04:05"
    assert convert("1:09 AM to 1:00 PM") == "01:09 to 13:00"

def test_invalid_input_1():
    with pytest.raises(ValueError):
        convert("9:00 to 5:00 PM")

def test_invalid_input_2():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")

def test_invalid_input_3():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

def test_invalid_input_4():
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")