import csv
import sys

def main():
    input_file, output_file = get_input_output_files()
    form_letter = read_csv_file(input_file)
    write_csv_file(output_file, form_letter)
    print(f"Converted {len(form_letter)} rows from {input_file} to {output_file}")

def get_input_output_files():
    if len(sys.argv) != 3:
        if len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        if len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")

    if not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        sys.exit("Not a CSV file")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    return input_file, output_file

def read_csv_file(input_file):
    form_letter = []
    try:
        with open(input_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                first, last = row['name'].split(",")
                # Swicth oder first and last name
                form_letter.append({'first': last.strip(), 'last': first.strip(), 'house': row['house']})
    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")

    return form_letter


def write_csv_file(output_file, form_letter):
    try:

        with open(output_file, 'w', newline='') as file:
            fieldnames = ['first', 'last', 'house']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(form_letter)
    except ValueError:
        sys.exit(f"Could not write {output_file}")

if __name__ == "__main__":
    main()