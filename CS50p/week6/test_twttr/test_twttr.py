import twttr

def test_shorten_word_without_vowels():
    assert twttr.shorten("bcdfghjklmnpqrstvwxyz") == "bcdfghjklmnpqrstvwxyz"

def test_shorten_word_with_vowels():
    assert twttr.shorten("Hello, world") == "Hll, wrld"

def test_shorten_without_capitalized_vowels():
    assert twttr.shorten("AHELLIOU") == "HLL"

def test_shorten_symbols():
    assert twttr.shorten("!@#$%^&*()_+") == "!@#$%^&*()_+"

def test_shorten_numbers():
    assert twttr.shorten("a1e2i3o4u5") == "12345"

def test_shorten_punctuation():
    assert twttr.shorten("What?! How did it happen? Come on be serious.") == "Wht?! Hw dd t hppn? Cm n b srs."

def test_shorten_empty():
    assert twttr.shorten("") == ""


if __name__ == "__main__":
    twttr.main()
