from numb3rs import validate

def test_validate():
    assert validate("192.168.0.14")
    assert validate("1.3.4.1")

def test_validate_invalid():
    assert not validate("192.168.0.256")
    assert not validate("256.256.256.256")