from PIL import Image

def load_image(file_path):
    # Open the image
    image = Image.open(file_path)
    # Return the image object
    return image

def resize_image(image, width, height):
    # Resize the image
    resized_image = image.resize((width, height))
    # Return the resized image object
    return resized_image

def convert_to_bw(img):
    # Convert the function object image to black and white
    bw_image = img.convert('L')
    # Return the black and white image object
    return bw_image

def save_image(image, file_path):
    # Save the image to file
    image.save(file_path)

def main():
    # Load the image
    image = load_image('./assets/me50.jpg')
    # Resize the image
    resized_image = resize_image(image, 800, 600)
    # Convert the image to black and white
    bw_image = convert_to_bw(resized_image)
    # Save the black and white image to file
    save_image(bw_image, './assets/me50_bw.jpg')


if __name__ == "__main__":
    main()