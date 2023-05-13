def main():
    month_names = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

    while True:
        date_input = input("Enter a date in MM/DD/YYYY or Month DD, YYYY format: ")

        # Strip leading and trailing spaces
        date_input = date_input.strip()

        # Split date input by '/' or ','
        if "/" in date_input:
            date_parts = date_input.split("/")
        elif "," in date_input:
            date_parts = date_input.replace(",", "").split(" ")
        else:
            print("Invalid date format. Please try again.")
            continue

        if len(date_parts) !=3:
            print("Invalid date format. Please try again.")
            continue

        # Identify and validate month
        month_str = date_parts[0].strip().capitalize()
        try:
            month = int(month_str)
        except ValueError:
            try:
                month = month_names.index(month_str) + 1

            except ValueError:
                print("Invalid month. Please try again.")
                continue

        if month < 1 or month > 12:
            print("Invalid month. Please try again.")
            continue

        # Validate day
        try:
            day = int(date_parts[1])
        except ValueError:
            print("Invalid day. Please try again.")
            continue

        if day < 1 or day > 31:
            print("Invalid day. Please try again.")
            continue

        # Validate year
        try:
            year = int(date_parts[2])
        except ValueError:
            print("Invalid year. Please try again.")
            continue

        # Check for leap year
        leap_year = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

        # Check for valid days in February
        if month == 2 and ((leap_year and day > 29) or (not leap_year and day > 28)):
            print("Invalid day. Please try again.")
            continue

        # Check for valid days in April, June, September, November
        if month in [4, 6, 9, 11] and day > 30:
            print("Invalid day. Please try again.")
            continue

        # Check if the original input was formatted correctly
        if date_input != f"{month}/{day}/{year}" and date_input != f"{month_names[month - 1]} {day}, {year}":
            print("Invalid date format. Please try again")
            continue

        # Format and print date in YYYY-MM-DD format
        print(f"{year}-{month:02}-{day:02}")
        break


if __name__ == "__main__":
        main()
