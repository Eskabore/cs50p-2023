### Response
The `is_valid_email()` function takes an email address as an argument and returns `True` if the address is syntactically valid according to the `validators` library's `email()` function, or `False` otherwise.

The `main()` function prompts the user to input an email address using `input()`, calls `is_valid_email()` to check the validity of the address, and prints either "Valid email address" or "Invalid email address" based on the result.

Finally, the `if __name__ == "__main__":` block ensures that `main()` is only called if the file is run as a script, rather than being imported as a module into another program.