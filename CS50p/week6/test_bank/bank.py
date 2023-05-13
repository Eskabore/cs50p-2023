def main():
    greeting = input("Pease enter a greting: ")
    result = value(greeting)
    print(f"{result}")



def value(greeting):
    """
    Returns a value based on the input string.
    If the string starts with "hello" (case-insensitive), return 0.
    If the string starts with "h" (case-insensitive), but not "hello", returns 20.
    Otherwise, returns 100.
    """
    greeting = greeting.lstrip().lower()
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()