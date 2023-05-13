import re
import sys


def main():
    try:
        text_input = input("Text: ")
        if not isinstance(text_input, str):
            raise TypeError("input must e a string")
        print(count(text_input))
    except Exception as e:
        print("Error: ", e)
        sys.exit(1)

def count(s):
    # se regex to find all occurences of "um" as a word
    matches = re.findall(r"\bum\b", s, re.IGNORECASE)
    return len(matches)


if __name__ == "__main__":
    main()

