# Define accepted denomination and price of Coke
denominations = [25, 10, 5]
price = 50

# Initialize varibles for tracking amount inserted and amount due and change owed
amount_inserted = 0
amount_due = price
change_owed = 0

# Prompt user to insert coins until price is reached
while amount_inserted < price:

    print("Amount Due:", amount_due)
    # Get user input
    coin = int(input("Insert coin: "))

    # Check if input is in accepted denomination
    if coin in denominations:

        # Add coin to total amount
        amount_inserted += coin

        # If amount due is greater than 0, update 'change_owed'
        if amount_due > 0:
            amount_due = price - amount_inserted
            change_owed = amount_due
else:
    # Print absolute value of amount due using `abs()`
    print("Change Owed:", abs(change_owed))