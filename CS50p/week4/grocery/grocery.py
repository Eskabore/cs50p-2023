from collections import Counter

grocery_list = []

while True:
    try:
        item = input("")
        grocery_list.append(item.lower())
    except EOFError:
        break

# Count the occurences of each item
item_counts = Counter(grocery_list)

# Sort the items aphabetically and convert them to uppercase
sorted_items = sorted(item_counts.keys(), key=str.lower)

# Print the grocery list with counts and uppercase items
for item in sorted_items:
    count = item_counts[item]
    print(f"{count} {item.upper()}")