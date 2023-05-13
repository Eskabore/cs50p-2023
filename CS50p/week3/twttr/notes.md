Explanation:

1.  The program prompts the user to enter some text using the `input()` function and stores it in the `text` variable.

2.  The program initializes a string variable called `vowels` with all the vowels in uppercase and lowercase.

3.  The program initializes an empty string variable called `new_text`, which will eventually hold the text with all vowels removed.

4.  The program loops through each letter in the `text` variable using a `for` loop.

5.  For each letter, the program checks if it is not in the `vowels` string using the `not in` operator.
    
6.  If the letter is not a vowel, the program adds it to the `new_text` string using the `+=` operator.

7.  After the loop is finished, the program prints out the `new_text` string, which contains the original text with all vowels removed.