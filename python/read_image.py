from PIL import Image
import timeit

def read_image():
    im = Image.open("../simple-pixels/1x1_WHITE.jpg")

    # Prints Image Format, Size NxN, and Mode
    print(im.format, im.size, im.mode)

    # Shows an Image
    im.show()

# Execution Time = .0214
print(timeit.timeit(read_image, number=1))