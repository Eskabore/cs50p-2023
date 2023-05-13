import pytest
from fuel import convert, gauge

def test_convert_100():
    assert convert("5/5") == 100

def test_convert_50():
    assert convert("1/2") == 50
    assert convert("3/6") == 50

def test_convert_zero():
    assert convert("0/1") == 0

def test_convert_value_error():
    with pytest.raises(ValueError):
        convert("a/b")

def test_convert_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_gauge_e():
    assert gauge(1) == "E"

def test_gauge_percenetage():
    assert gauge(2) == "2%"
    assert gauge(50) == "50%"
    assert gauge(75) == "75%"

def test_gauge_f():
    assert gauge(99) == "F"
