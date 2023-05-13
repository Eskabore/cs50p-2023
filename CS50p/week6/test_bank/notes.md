**`bank.py`**
An implementation of the `value` function for Home Federal Savings Bank, as well as a `main` function and a `if __name__ == "__main__":` block to test the function:

In this implementation, `value` takes in a string `greeting`, checks if it starts with "hello" or "h" (case-insensitive) and returns the corresponding value. The `main` function simply calls `value` with three different inputs and prints out the resulting values.

**`test_bank.py`**
In this test file, we import the `value` function from `bank` and define several test cases. The test cases cover a range of inputs, including strings starting with "hello", "h", and other letters, as well as empty strings, numbers, and special characters. We use `assert` statements to check that the values returned by `value` match the expected values.