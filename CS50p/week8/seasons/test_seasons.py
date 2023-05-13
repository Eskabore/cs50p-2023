from datetime import date, timedelta
from seasons import calculate_age_in_minutes, convert_number_to_words

def test_get_age_in_minutes():
    birth_date = date(2000, 1, 1)
    today = date(2023, 5, 1)
    delta = today - birth_date
    expected_minutes = round(delta.total_seconds() / 60)
    assert calculate_age_in_minutes(birth_date) == expected_minutes

    birth_date = date(1990, 12, 12)
    today = date(2023, 5, 1)
    delta = today - birth_date
    expected_minutes = round(delta.total_seconds() / 60)
    assert calculate_age_in_minutes(birth_date) == expected_minutes

def test_convert_number_to_words():
    assert convert_number_to_words(123456) == "One hundred twenty-three thousand, four hundred fifty-six"
    assert convert_number_to_words(1) == "One"