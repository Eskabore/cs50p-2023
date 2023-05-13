def process_greeting(greeting):
    greeting = greeting.lstrip().lower()
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100

greeting = input("Please enter a greeting: ")
result = process_greeting(greeting)
print(f"${result}")