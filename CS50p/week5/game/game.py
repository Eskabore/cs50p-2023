import random


def get_positive_integer(prompt):
    # Prompt user for a positive integer
    while True:
        value = input(prompt)
        if value.isdigit() and int(value) > 0:
            return int(value)
        else:
            print("Invalid input")


def play_guessing_game(n):
    # Generates random number between 1 and n and prompts the user to guess the number
    random_number = random.randint(1, n)
    while True:
        guess = get_positive_integer(
            "Guess the integer between 1 and {}: ".format(n))
        if guess < random_number:
            print("Too small!")
        elif guess == random_number:
            print("Just right!")
            break
        else:
            print("Too large!")


def main():
    # Gets the maximum value of the range from the user and calls play_guessing_game to play the game
    n = get_positive_integer("Level (Enter a positive integer: ")
    play_guessing_game(n)

# Call the main function when the script is run
if __name__ == "__main__":
    main()
