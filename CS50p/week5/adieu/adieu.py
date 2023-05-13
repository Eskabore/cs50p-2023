import inflect

# Initialize an empty list
names = []

# Enter a loop that reads names from the user until the user inputs control-d
while True:
    try:
        name =  input("Name: ") # Read a name from the user
        names.append(name) # Append the name to the `name` list
    except EOFError: # Catch the EOFError that is raised when the user inputs control-d
        break

# Check how many names were entered
n = len(names)
if n == 1:
    # Print a simple farewell message with the only name entered
    print("Adieu, adieu, to {}.".format(names[0]))
elif n == 2:
    # Print a farewell message with both names separated by "and"
    print("Adieu, adieu, to {} and {}.".format(names[0], names[1]))
elif n == 3:
    # Print a farewell message with two comms and one `and`
    print("Adieu, adieu, to {}, {}, and {}.".format(names[0], names[1], names[2]))
    # Print `n` names with `n-1` commas and one `and`
elif n > 3:
    p = inflect.engine()
    namelist = p.join(names)
    print("Adieu, adieu, to {}.".format(namelist))