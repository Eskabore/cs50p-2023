def calculate(expression):
    # Split the expression into its constituent parts
    x, y, z = expression.split()
    x = int(x)
    z = int(z)

    # Use a dictionary to map the operator to the appropriate function
    operators = {
        "+": lambda x, z: x + z,
        "-": lambda x, z: x - z,
        "*": lambda x, z: x * z,
        "/": lambda x, z: x / z
    }

    # Use the operator dictionary to perform the appropriate arithmetic
    result = operators[y](x, z)

    # Format the result as a float with one decimal place and print it
    print("{:.1f}".format(result))

# Prompt the user for an expression and pass it to the calculate function
expression = input("Expression: ")
calculate(expression)