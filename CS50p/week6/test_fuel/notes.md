```python
def test_convert_valueerror():
    try:
        convert("a/b")
    except ValueError as e:
        assert str(e) == "Values must be integers"
    try:
        convert("1/0")
    except ZeroDivisionError as e:
        assert str(e) == ("Denominator cannot be zero")
```

**`test_fuel_py`**:
This code is a Python script that contains a set of tests for the convert() and gauge() functions in a module called fuel. The tests are implemented using the pytest library.

The test_convert_100() function checks if convert() correctly calculates the percentage of fuel in a tank when the tank is full (100% full). It uses two test cases with different fractions.

The test_convert_50() function checks if convert() correctly calculates the percentage of fuel in a tank when the tank is half full (50% full). It uses two test cases with different fractions.

The test_convert_zero() function checks if convert() correctly calculates the percentage of fuel in a tank when the tank is empty (0% full).

The test_convert_value_error() function checks if convert() raises a ValueError when the fraction passed as an argument is invalid.

The test_convert_zero_division() function checks if convert() raises a ZeroDivisionError when the denominator of the fraction passed as an argument is zero.

The test_gauge_e() function checks if gauge() returns the correct value ("E") when the percentage of fuel in the tank is less than or equal to 1%.

The test_gauge_percentage() function checks if gauge() correctly formats the percentage of fuel in the tank when it is between 2% and 75%.

The test_gauge_f() function checks if gauge() returns the correct value ("F") when the percentage of fuel in the tank is greater than or equal to 99%.