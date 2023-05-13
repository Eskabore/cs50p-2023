Here's how the programm works:

-   The `main` function is the entry point of the program. It first calls `get_level` to prompt the user for a level and store it in the `level` variable.
-   It then generates a list of 10 math problems by calling `generate_integer` twice for each problem and concatenating the results with the `+` and `=` signs.
-   It initializes the `score` variable to 0.
-   It then loops through the list of problems and for each problem, it enters a loop that allows the user up to 3 attempts to answer the problem correctly.
-   In each attempt, it prompts the user for an answer using the `input` function, tries to convert the answer to an integer using `int`, and checks if the integer is equal to the correct answer of the problem, which is computed by evaluating the string expression without the `=` sign using `eval`.
-   If the answer is correct, it increments the `score` variable and breaks out of the loop to move on to the next problem.
-   If the answer is incorrect or not even a number, it prints "EEE". If the user has already attempted 3 times, it prints the correct answer of the problem and moves on to the next problem.
-   After all problems are solved, it prints the user's score.

The `get_level` function prompts the user for a level and keeps prompting until the user enters a valid level (1, 2, or 3).

The `generate_integer` function takes a level as input and returns a random integer with the specified number of digits, based on the level. If the level is not 1, 2, or 3, it raises a `ValueError`.