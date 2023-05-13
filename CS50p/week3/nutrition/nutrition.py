fruit_calories = {
    'Apple': 130,
    'Avocado': 50,
    'Banana': 110,
    'Cantaloupe': 50,
    'Grapefruit': 60,
    'Grapes': 90,
    'Honeydew Melon': 50,
    'Kiwifruit': 90,
    'Lemon': 15,
    'Lime': 20,
    'Nectarine': 60,
    'Orange': 80,
    'Peach': 60,
    'Pear': 100,
    'Pineapple': 50,
    'Plums': 70,
    'Strawberries': 50,
    'Sweet Cherries': 100,
    'Tangerine': 50,
    'Watermelon': 80
}

# Convert the dictionary keys to lowercase
fruit_calories = {k.lower(): v for k, v in fruit_calories.items()}

# Prompt the user for a fruit input and convert it to lowercase
fruit_input = input("Enter a fruit: ").lower()



# Check if the fruit exists in the dictionary and output its calorie count if it does
if fruit_input in fruit_calories:
    print(f"{fruit_input} has {fruit_calories[fruit_input]} calories per portion.")
# else:
    # print("Sorry, that's not a fruit.")