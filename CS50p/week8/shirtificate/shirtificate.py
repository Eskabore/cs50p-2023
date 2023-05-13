import os
import sys
from fpdf import FPDF, XPos, YPos
from PIL import Image

class Shirtificate(FPDF):
    def __init__(self, name: str):
        super().__init__(orientation='P', unit='mm', format='A4')
        self.name = name

    def get_image_dims(self, image_path):
        with Image.open(image_path) as img:
            width, height = img.size
        return width, height

    def create_shirtificate(self):

        self.set_auto_page_break(False)

        # Add a new page
        self.add_page()
        # Set the font and size
        self.set_font("Helvetica", size=24, style="B")
        # Add the title of the shirtificate
        self.cell(0, 10, "CS50 Shirtificate", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_font("Helvetica", size=16)
        self.cell(0, 10, f"Congratulations, {self.name}!", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        # self.set_text_color(255, 255, 255)

        image_path = os.path.join(".", "shirtificate.png")

        try:
            image_width, image_height = self.get_image_dims(image_path)
            # Get the position to center the image
            image_x = (self.w - image_width * self.k) / 2
            image_y = self.get_y() + 10
            # Add the image to the shirtificate
            self.image(image_path, x=image_x, y=image_y, w=image_width, h=image_height)
            # Save the shirtificate as a PDF file
            self.output("shirtificate.pdf")
        except Exception as e:
            print(f"An error occured while creating the shirtificate: {e}")
            sys.exit(1)


def main():
    try:
        # Prompt user for name
        name = input("Enter your name: ")
        # Create a new instance of the Shirtificate class with input
        shirtificate = Shirtificate(name)
        # Create the shirtificate
        shirtificate.create_shirtificate()
        print("Shirtificate created: shirtificate.pdf")
    except Exception as e:
        print(f"An error occured: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()