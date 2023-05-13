### 1. Project Structure

First, let's organize the project:

```
image_editor/
├── project.py
├── test_project.py
└── requirements.txt
```

### 2. Requirements

In `requirements.txt` file, we need to include the Pillow library. This is a powerful library for opening, manipulating, and saving many different image file formats.

```
Pillow
pytest
```

### 3. Functions

In `project.py` file, we'll need to implement `main` function and at least three other functions. Here's a possible set of functions:

1. `load_image(file_path)`: This function should take a file path as input, open the image at that location, and return the image object.

2. `resize_image(image, width, height)`: This function should take an image object and desired width and height as input, resize the image, and return the resized image.

3. `convert_to_bw(image)`: This function should take an image object, convert it to black and white, and return the converted image.

4. `save_image(image, file_path)`: This function should take an image object and a file path, and save the image at the given location.

### 4. Testing

In `test_project.py` file, we should implement tests for each of the above functions. For example:

1. `test_load_image()`: This could check that an image is correctly loaded, maybe by checking that the returned object is an instance of the correct class.

2. `test_resize_image()`: This could check that an image is correctly resized, maybe by comparing the dimensions of the output image to the expected dimensions.

3. `test_convert_to_bw()`: This could check that an image is correctly converted to black and white, perhaps by checking that the output image's mode is 'L' (the mode Pillow uses for grayscale images).

4. `test_save_image()`: This could check that an image is correctly saved, possibly by checking that a file is created at the expected location.

### 5. Main Function

Finally, `main` function should tie everything together. It might take a file path as input, load the image from that file, resize it and convert it to black and white, then save it at a new location.