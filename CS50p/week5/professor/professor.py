import random


def main():
    # Prompt the user for a level
    level = get_level()

    # Generate 10 math problems with n digits each
    problems = []
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        problem = f"{x} + {y} = "
        problems.append(problem)

    # Prompt the user to solve each probem,allowing up to 3 tries
    score = 0
    for problem in problems:
        for i in range(3):
            answer = input(problem)
            try:
                if int(answer) == eval(problem[:-2]):
                    score += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
        else:
            print(f"The correct answer is {eval(problem[:-2])}")

    # Output the user score
    print(f"{score}")
    print("Thank you for playing")


def get_level():
    while True:
        level = input("Enter a difficulty level (1, 2, or 3): ")
        if level in ["1", "2", "3"]:
            return int(level)


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError


if __name__ == "__main__":
    main()
