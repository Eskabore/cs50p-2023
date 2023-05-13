import sys
import validators

def is_valid_email(email):
    return validators.email(email)

def main():
    try:
        email = input("Please enter an email address: ")
        if is_valid_email(email):
            print("Valid")
        else:
            print("Invalid")
    except KeyboardInterrupt:
        print("\nProgram terminated by user")
        sys.exit(1)
    except Exception as e:
        print("Error: ", e)
        sys.exit(1)


if __name__ == "__main__":
    main()