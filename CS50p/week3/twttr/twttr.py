text = input("Input: ")
vowels = "AEIOUaeiou"
new_text = ""

for letter in text:
    if letter not in vowels:
        new_text += letter

print(new_text)