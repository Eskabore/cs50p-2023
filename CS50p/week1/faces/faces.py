def convert(text):
    return text.replace(":)", "🙂").replace(":(", "🙁")


def main():
    user_input = input("Enter some text: ")
    converted_text = convert(user_input)
    print("Converted text:", converted_text)

if __name__ == "__main__":
    main()
