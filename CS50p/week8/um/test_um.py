from um import count

def test_count_0_um():
    assert count("hello, world!") == 0

def test_oount_1_um():
    assert count("um?") == 1
    assert count("Um, thanks for the album") == 1

def test_count_multiple_um():
    assert count("Um, thanks, um...") == 2
    assert count("I am, um, trying, um, to think of words, um umm") == 3

