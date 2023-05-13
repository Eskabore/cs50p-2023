def get_fraction():
    # Loop until a valid function is entered
    while True:
        try:
            # Prompt the user for a fraction and parse it into two integers
            fraction = input("Enter fuel fraction (X/Y): ")
            x, y = fraction.split("/")
            x, y = int(x), int(y)
            # Check if the integers satisfy the conditions for a valid fraction
            if x < 0 or y <= 0 or x > y:
                raise ValueError("Invalid fraction")
            # Return the parsed integers if they are valid
            return x, y
        except (ValueError, ZeroDivisionError) as e:
            # Catch any exceptions that might be raised
            # print an error message
            # prompt for a new fraction
            print(f"Error: {e}. Please enter a valid fraction.")


def main():
    # Call get_fraction() to get a valid fraction from the user
    x, y = get_fraction()
    # Calculate the percentage of fuel in the tank and round it to the nearest integer
    percentage = round(x/y * 100)
    # Check if the tank is essentially empty or full, or output percentage as string
    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%")


# Call rhe main() function if this script is run as the main module
if __name__ == "__main__":
    main()
