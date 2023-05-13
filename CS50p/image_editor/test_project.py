import pytest
from PIL import Image
from project import load_image, resize_image, convert_to_bw, save_image

@pytest.fixture
def example_image():
    return Image.new('RGB', (800, 600), color='red')


def test_load_image(tmp_path, example_image):
    # Save image to temporary file
    file_path = tmp_path / 'test.image.jpg'
    example_image.save(file_path)

    # Load the image from the temporary file
    loaded_image = load_image(str(file_path))

    # Assert that the loaded image is the same as the image
    assert loaded_image.size == example_image.size
    assert loaded_image.mode == example_image.mode

def test_resize_image(example_image):
    # Resize the image to hal its original size
    resized_image = resize_image(example_image, 400, 300)

    # Assert that the resized image haas the expected dimensions
    assert resized_image.size == (400, 300)

def test_convert_to_bw(example_image):
    # Convert the image to black and white
    bw_image = convert_to_bw(example_image)

    # Assert that the resulting image is in grayscale mode
    assert bw_image.mode == 'L'

def test_save_image(tmp_path, example_image):
    # Save the image to a temporary file
    file_path = tmp_path / 'test_image.jpg'
    save_image(example_image, str(file_path))

    # Load the saved image from the temporary file
    loaded_image = Image.open(file_path)

    # Assert that the loaded image is the same as the image
    assert loaded_image.size == example_image.size
    assert loaded_image.mode == example_image.mode