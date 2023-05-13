This program prompts the user to enter items for their grocery list, one at a time, until the user enters the "end of file" character (Ctrl+D on most systems). The program converts each item to lowercase to make the input case-insensitive, and stores it in a list.

After the user is finished inputting items, the program uses the `Counter` class from the `collections` module to count the occurrences of each item in the list. The program then sorts the items alphabetically, ignoring case, and converts them to uppercase.

Finally, the program loops through the sorted items and prints each one with a count of how many times the user entered that item.