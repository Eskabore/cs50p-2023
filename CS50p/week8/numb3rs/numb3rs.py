import re
import sys

"""
In a file called numb3rs.py, implement a function called validate that expects an IPv4 address as input as a str
and then returns True or False, respectively, if that input is a valid IPv4 address or not.
"""


# Check if the IP address is valid using regular expression
def validate(ip_input):
    pattern = r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"

    if re.match(pattern, ip_input):
        return True
    else:
        return False

# Print the result
def main():
    try:
        ip_address = input("IPv4 address: ").strip()
        if validate(ip_address):
            print("Valid IPv4 address")
        else:
            print("Invalid IPv4 address")
    except KeyboardInterrupt:
        sys.exit(1)
    except EOFError:
        sys.exit(1)


if __name__ == "__main__":
    main()