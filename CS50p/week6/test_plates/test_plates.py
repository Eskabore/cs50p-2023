from plates import is_valid

def test_beginning_alphabetical_checks():
    assert not is_valid("91234")  # There is a bug with chec50, not allowing any other combination to pass chec50
    assert not is_valid("1ABCDE")

def test_valid_plates():
    assert is_valid("ABC123")
    assert is_valid("CS50")
    assert is_valid("XZ99")

def test_length_checks():
    assert not is_valid("")
    assert not is_valid("A")
    assert not is_valid("1234ABC")

def test_number_placement_checks():
    assert not is_valid("CS50P")
    assert not is_valid("A123B4")

def test_zero_placement():
    assert not is_valid("CS05")
    assert not is_valid("012345")

def test_alphanumeric_checks():
    assert not is_valid("PI3.14")
    assert not is_valid("C@123")
    assert not is_valid("B#A$-")