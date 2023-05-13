def camel_to_snake(camel_str):
    # Replace capital letters with underscore followed by lowercase version of the letter
    snake_str = ""
    for i, c in enumerate(camel_str):
        if c.isupper() and i > 0:
            snake_str += "_" + c.lower()
        else:
            snake_str += c

    return snake_str


def main():
    # Prompt the user for the name of a variable in camel case
    camel_name = input("camelCase: ")

    # Convert the variable name to snake case
    snake_name = camel_to_snake(camel_name)

    # Output the corresponding name in snake case
    print("snake_case:", snake_name)


if __name__ == "__main__":
    main()
