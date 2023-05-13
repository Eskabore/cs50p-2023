from bank import value

def test_value_entire_phrase():
    assert value("hello, world") == 0

def test_value_entire_phrase_case_insensitivity():
    assert value("HELLO, WORLD") == 0

def test_value_hello():
    assert value("hello") == 0

def test_value_hello_case_insensitive():
    assert value("HELLO") == 0

def test_value_h():
    assert value("h") == 20

def test_value_h_case_insensitive():
    assert value("H") == 20

def test_value_other_word():
    assert value("Goodbye") == 100

def test_value_empty_string():
    assert value("") == 100

def test_value_numbers():
    assert value("1234") == 100

def test_value_special_characters():
    assert value("~!@#$%^&*()_+") == 100