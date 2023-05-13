# Prompt user to enter a string of text
text = input("Input: ")

# Initialize an empty string to store the modified text
modified_text = ""

# Loop through each character in the input string
for char in text:
    # Check if the character is a vowel, regardless of case
    if char.lower() in "aeiou":
        # If it's vowel, skip character and move to next
        continue
    else:
        # If it's not vowel, add it to the modified text string
        modified_text += char

# Output modified text to the console
print("Output:", modified_text)