import re
import sys

def main():
    time_input = input("Hours: ")
    try:
        print(convert(time_input))
    except ValueError as e:
        print(e)
        sys.exit(1)

def convert(s):
    # Define regex pattern for both 12-hour formats
    pattern1 = r"(\d{1,2}):(\d{2})\s*(AM|PM)\s*to\s*(\d{1,2}):(\d{2})\s*(AM|PM)"
    pattern2 = r"(\d{1,2}) (AM|PM) to (\d{1,2}) (AM|PM)"

    # Match input string with both patterns
    match1 = re.search(pattern1, s)
    match2 = re.search(pattern2, s)

    if match1:
        start_hour, start_min, start_ampm, end_hour, end_min, end_ampm = match1.groups()
        # Convert start hour to 24-hour format
        if start_ampm == "PM" and start_hour != "12":
            start_hour = str(int(start_hour) + 12).zfill(2)
        elif start_ampm == "AM" and start_hour == "12":
            start_hour = "00"

        # Convert end hour to 24-hour format
        if end_ampm == "PM" and end_hour != "12":
            end_hour = str(int(end_hour) + 12).zfill(2)
        elif end_ampm == "AM" and end_hour == "12":
            end_hour = "00"

    elif match2:
        start_hour, start_ampm, end_hour, end_ampm = match2.groups()
        start_min, end_min = "00", "00"

        # Convert start hour to 24-hour format
        if start_ampm == "PM" and start_hour != "12":
            start_hour = str(int(start_hour) + 12).zfill(2)
        elif start_ampm == "AM" and start_hour == "12":
            start_hour = "00"

        # Convert end hour to 24-hour format
        if end_ampm == "PM" and end_hour != "12":
            end_hour = str(int(end_hour) + 12).zfill(2)
        elif end_ampm == "AM" and end_hour == "12":
            end_hour = "00"
    else:
        raise ValueError("ValueError")

    # Check for valid hours and minutes
    for hours, minutes in [(start_hour, start_min), (end_hour, end_min)]:
        if int(hours) > 23 or int(minutes) > 59:
            raise ValueError("ValueError")

    # Format output string with leading zeros for hours and minutes
    return f"{start_hour.zfill(2)}:{start_min.zfill(2)} to {end_hour.zfill(2)}:{end_min.zfill(2)}"


if __name__ == "__main__":
    main()
