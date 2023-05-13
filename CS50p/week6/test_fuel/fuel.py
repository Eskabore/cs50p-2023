def convert(fraction):
    # Split the fraction into its numerator and denominator
    x, y = str(fraction).split('/')

    # Check if both parts are integers
    if not x.isdigit() or not y.isdigit():
        raise ValueError("Values must be integers")
    # Check if denominator is zero (placed here in order to pass check50)
    elif int(y) == 0:
        raise ZeroDivisionError("Denominator cannot be zero")
    elif int(x) > int(y):
        raise ValueError("Invalid fraction")
    return round(int(x) / int(y) * 100)

def gauge(percentage):
    # Check if tank is essentially empty or full, otherwise output percentage of fuel remaining
    if percentage <= 1:
        return "E"
    if percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

def main():
    # Loop until a valid fraction is entered
    while True:
        try:
            fraction = input("Enter a fraction formatted as X/Y: ")
            # Output gauge level (in form fx(fy(z)) in order to pass pytest without error message)
            print(gauge(convert(fraction)))
            break
        # Catch exceptions and print error messages from convert()
        except (ValueError, ZeroDivisionError) as e:
            print(e)

# Call the main() function if this script is run as the main module
if __name__ == "__main__":
    main()
