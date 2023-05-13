# Define a function to convert a time string to the corresponding number of hours
def convert(time_str):
    # Check if the suffix is present
    if "a.m." in time_str or "p.m." in time_str:
        # Split thhe time string into hours, minutes, and suffix
        time_str, suffix = time_str.split(" ")
        hours, minutes = map(int, time_str.split(":"))

        # Convert hours to 24-hour format
        if suffix.lower() == "p.m.":
            hours += 12

    else:
        # Split the time string into hours and minutes
        hours, minutes = map(int, time_str.split(":"))

    # Return the total number of hours
    return hours + minutes / 60


def main():
    # Prompt the user for a time in 24-hour format
    time_str = input("Please enter a time in 12-hour or 24-hour format (e.g, 07:30 or 7:30 a.m): ")

    # Convert the time to the corresponnding number of hours
    time_hours = convert(time_str)

    # Determine whether it's breakfast, lunch, or dinner time
    if 7 <= time_hours <= 8:
        print("breakfast time")
    elif 12 <= time_hours <= 13:
        print("lunch time")
    elif 18 <= time_hours <= 19:
        print("dinner time")

    # If it's not time for a meal, don't output nothin


# Call main functtion
if __name__ == "__main__":
    main()
