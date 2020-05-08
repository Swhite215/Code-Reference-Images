from PIL import Image
import timeit

def change_pixel():
    im = Image.open("../simple-pixels/1x1_WHITE.jpg");

    # Convert Image to Pixel Map
    pixels = im.load()

    # Change A Single Pixel to Different Color
    pixels[0,0] = (0,255,0,255)

    # Check Results
    im.show()

print(timeit.timeit(change_pixel, number=1))