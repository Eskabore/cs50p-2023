import emoji


def emojize_text(text):
    # Replace aliases with corresponding codes
    text = emoji.emojize(text, language='alias')
    # Replace codes with corresponding emojis
    text = emoji.emojize(text)
    return text


if __name__ == "__main__":
    # Prompt user for input
    input_text = input("Input: ")
    # Emojize input and print the result
    emojized_text = emojize_text(input_text)
    print(f"Emojized string: {emojized_text}")