from PIL import Image
import sys
def convert_to_grey_scale(image_path):
    with Image.open(image_path) as img:
        grey_img = img.convert('L')
        grey_img.save('greyscale_image.jpg')

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python convert_to_greyscale.py [image_path]")
    else:
        convert_to_grey_scale(sys.argv[1])