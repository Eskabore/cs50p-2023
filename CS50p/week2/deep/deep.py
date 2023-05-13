def main():
    answer = input("What is the answer to the Great Question of Life, the Universe, and everything? ")
    answer = answer.replace(" ", "")
    if answer.lower() in ["42", "fortytwo", "forty-two"]:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()