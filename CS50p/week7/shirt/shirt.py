import os, sys
from PIL import Image, ImageOps

def main():
    # Checks conditions with appropriate error message
    if len(sys.argv) != 3:
        sys.exit("Usage: python shirt.py <argument1> <argument2>")

    input_file, output_file = sys.argv[1], sys.argv[2]

    validate_input(input_file, output_file)
    resize_and_overlay(input_file, output_file)


# Checks conditions with appropriate error message
def validate_input(input_file, output_file):
    input_ext = os.path.splitext(input_file)[1].lower()
    output_ext = os.path.splitext(output_file)[1].lower()

    if not (input_ext in ('.jpg', '.jpeg', '.png') and output_ext in ('.jpg', '.jpeg', '.png')):
        sys.exit("Input and output files must be .jpg, .jpeg, or .png files")

    if input_ext != output_ext:
        sys.exit("Input and output have different extensions")

    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file {input_file} does not exist")



def resize_and_overlay(input_file, output_file):
    # Open input image
    with Image.open(input_file) as input_img:


        # Open shirt image with transparent background
        shirt_file = os.path.join(os.path.dirname(__file__), 'shirt.png')
        if not os.path.exists(shirt_file):
            raise FileNotFoundError(f"Shirt file {shirt_file} does not exist")
        with Image.open(shirt_file) as shirt:
            size = shirt.size
            
            # Resize and crop input image to the same size as shirt image
            input_img = ImageOps.fit(input_img,size, method=Image.BICUBIC, bleed=0.0, centering=(0.5, 0.5))

            # Resize shirt image to match input image size
            shirt = shirt.resize(size, resample=Image.LANCZOS)

            # Overlay shirt on input image
            input_img.paste(shirt, (0, 0), mask= shirt)

            # Save result as output image
            input_img.save(output_file)
            print(f"Saved result as {output_file}")


if __name__ == "__main__":
    main()
