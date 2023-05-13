# Define a dictionnary of menu items and their prices
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

# Calculate and display the sum cost of all items
def display_total_cost(items):
    total_cost = sum([menu[item] for item in items])
    print(f"Total: ${total_cost:.2f}")


def main():
    # Initialize an empty list of items
    items = []
    # Loop to prompt the user for input
    while True:
        try:
            # Prompt the user for input and titlecase it
            item = input("Item: ").strip().title()
        except EOFError:
            # If the user presses control+d, exit the loop
            break

        # If the item is not in the menu, ignore it
        if item not in menu:
            continue

        # Add the item to the list of items and display the total cost
        items.append(item)
        display_total_cost(items)



if __name__ == "__main__":
    main()