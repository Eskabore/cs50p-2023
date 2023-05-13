def main():
    """
    Prompts the user for a vanity plate and prints "Valid" if it is valid or invalid if not.
    """

    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not s:
        return False

    min_length, max_length = 2, 6

    if not (min_length <= len(s) <= max_length):
        return False

    if s[0].isalpha():
        if not s[1].isalpha():
            return False

        has_number = False
        for i, c in enumerate(s):
            if c.isdigit():
                if i == 2 and c == '0':
                    return False
                has_number = True
            elif has_number:
                return False
    elif s[0].isdigit():
        if s[0] == '0':
            return False
        if not s.isdigit():
            return False
    else:
        return False

    return True


if __name__ == "__main__":
    main()
