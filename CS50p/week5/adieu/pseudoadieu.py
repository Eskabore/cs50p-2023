import inflect

# Initialize an empty list
names = []

# Enter a loop that reads names from the user until the user inputs control-d
while True:
    try:
        name =  input() # Read a name from the user
        names.append(name) # Append the name to the `name` list
    except EOFError: # Catch the EOFError that is raised when the user inputs control-d
        break

# Check how many names were entered
n = len(names)
if n == 1:
    # Print a simple firewall message with the only name entered
    print("Adieu, adieu, to {}".format(names[0]))
elif n == 2:
    # Print a farewell message with both names separated by "end"
    print("Adieu, adieu, to {} and {}.".format(names[0], names[1]))
elif n > 2:
    # Print a farewell message with all but the last name separated by commas
    # and the last name separated by 'and'
    print("Adieu, adieu, to ", end="")
    for i in range(n-1):
        print("{}, ".format(names[i]), end="")
    print("and {}.".format(names[-1]))