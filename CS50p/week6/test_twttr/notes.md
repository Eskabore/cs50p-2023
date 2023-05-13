# Twttr.py

This Python script aims to remove vowels from an input string while preserving other characters, such as digits and punctuation marks. The program can be used as a simple text transformation tool for various purposes.

## Code Overview

The program consists of two primary functions: `main()` and `shorten(word)`.

### main()

The `main()` function handles user input and output. It prompts the user to enter a text string, which is then passed to the `shorten()` function. The shortened string, with vowels removed, is then printed to the console.

### shorten(word)

The `shorten()` function takes a string input `word` and iterates through each character in the string. If the character is a digit, it is added directly to the new string `new_word`. If the character is not a vowel (neither uppercase nor lowercase), it is also added to the new string. Vowels are effectively omitted from the resulting string.

## Test Cases

The `test_twttr.py` file contains a series of test cases to ensure the functionality of the `twttr.py` program. The test cases cover the following scenarios:

1.  Test if the `shorten()` function correctly removes vowels and retains other characters in a string with no vowels.
2.  Test if the `shorten()` function removes vowels from a string containing both vowels and other characters.
3.  Test if the `shorten()` function removes only capitalized vowels from a string containing capitalized vowels and other characters.
4.  Test if the `shorten()` function retains symbols and special characters when provided with a string containing various symbols and special characters.
5.  Test if the `shorten()` function keeps digits in the output string when the input string contains a mix of alphabetic characters and digits.
6.  Test if the `shorten()` function retains punctuation marks when provided with a string containing various punctuation marks.
7.  Test if the `shorten()` function returns an empty string when given an empty input string.

When the `twttr.py` program is run with the provided test cases in `test_twttr.py`, the tests should pass, demonstrating the program's correctness and functionality.