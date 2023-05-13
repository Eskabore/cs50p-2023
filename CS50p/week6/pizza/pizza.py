import sys
import csv
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith('.csv'):
    sys.exit("Not a CSV file")

filename = sys.argv[1]

try:
    with open(filename, 'r', encoding='UTF-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        data = list(reader)
except FileNotFoundError:
    sys.exit("File does not exit")

# Convert the data to a list of lists
table = []
for row in data:
    table.append(row)

# Format the table using tabulate
headers = table[0]
rows = table[1:]
formatted_table = tabulate(rows, headers, tablefmt='grid')

# Print the formatted table
print(formatted_table)

