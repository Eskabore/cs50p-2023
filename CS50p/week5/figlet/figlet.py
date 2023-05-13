import sys
import random
from pyfiglet import Figlet

def main():
    # Check the command-line arguments
    if len(sys.argv) not in [1, 3]:
        sys.exit("Usage: python figlet.py [-f| --font FONT_NAME]")

    use_random_font = True
    font_name = ""

    if len(sys.argv) == 3:
        if sys.argv[1] not in ["-f", "--font"]:
            sys.exit("Invalid option. Use -f or --font followed by a font name.")
        else:
            font_name = sys.argv[2]
            if font_name not in Figlet().getFonts():
                sys.exit("fonts not found/ Check available fonts at figlet.org/examples.html.")
            use_random_font = False

    # Prompt the user for a string text
    text = input("Enter the next you want to display: ")

    # Initialize the Figlet object with the desired font
    figlet =  Figlet()

    if use_random_font:
        font_name = random.choice(figlet.getFonts())

    figlet = Figlet(font=font_name)

    # Output the text in the desired font
    print(figlet.renderText(text))

if __name__ == "__main__":
    main()