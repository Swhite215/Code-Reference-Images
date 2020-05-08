#generate_numpy.py
from PIL import Image
import numpy as np
import timeit

def change_all_pixels():
    targetColor = [0, 0, 0, 255]

    oldImagePath = "../simple-pixels/2x2_CARTESIAN_TEST.png"
    newImagePath = "../new-images/2x2_CARTESTIAN_BLACK.png"

    im = Image.open(oldImagePath)

    # Convert Image to NumpyArray
    numArray = np.array(im)

    # Get Pixels
    width = im.size[0]
    height = im.size[1]

    # Change Each Pixel to Target Color
    for row in range(width):
        for column in range(height):
            print(numArray[row, column])
            numArray[row, column] = [0, 0, 0, 255]

    # Convert NumpyArray to Image
    imageFromArray = Image.fromarray(numArray)

    # Show Old Image
    im.show()

    # Show New Image
    imageFromArray.show()

    # Save New Image
    imageFromArray.save(newImagePath)


change_all_pixels()

# Execution Time = .007
#print(timeit.timeit(change_all_pixels, number=1))

