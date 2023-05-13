The `pizza.py` program that reads a CSV file in Pinocchio's format and outputs a table formatted as **ASCII art** using tabulate package.

This program first checks if there is exactly one command-line argument, if the argument ends with .csv, and if the file exists. If any of these conditions is not satisfied, the program exits via sys.exit.
If all the conditions are satisfied, the program:
- reads the CSV file using the csv module,
- converts the data to a list of lists,
- formats the table using tabulate package with 'grid' table format,
- and finally prints the formatted table.