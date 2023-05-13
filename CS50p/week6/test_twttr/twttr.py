def main():
    text = input("Input: ")
    shortened_word = shorten(str(text))
    print(shortened_word)

def shorten(text):
    vowels = "AEIOUaeiou"
    new_word = ""

    for letter in text:
        if letter not in vowels:
            new_word += letter

    return new_word

if __name__ == "__main__":
    main()