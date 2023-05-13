import sys
from datetime import date
import inflect

def main():
    birth_date_str = input("Enter date of birth (YYYY-MM-DD): ")

    try:
        birth_date = date.fromisoformat(birth_date_str)
    except ValueError:
        print("Invalid date format. Please use format YYYY-MM-DD")
        sys.exit(1)

    minutes = calculate_age_in_minutes(birth_date)
    minutes_in_words = convert_number_to_words(minutes)
    print(f"{minutes_in_words} minutes")

def calculate_age_in_minutes(birth_date):
    today = date.today()
    delta = today - birth_date
    age_in_minutes = delta.total_seconds() / 60
    return round(age_in_minutes)

def convert_number_to_words(number):
    p = inflect.engine()
    words = p.number_to_words(number, andword='')
    return words.capitalize()



if __name__ == "__main__":
    main()