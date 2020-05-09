
from PIL import Image
import numpy as np
import timeit

def change_all_pixels():
    targetColor = [0, 0, 0, 255]

    oldImagePath = "../complex-pixels/ECRIC_UNCOLORIZED.png"
    newImagePath = "../new-images/ECRIC_BLACKED.png"

    im = Image.open(oldImagePath)

    print(im.format, im.size, im.mode)

    # Convert Image to NumpyArray
    numArray = np.array(im)

    print(numArray.shape[0])
    print(numArray.shape[1])

    # Get Pixels
    width = numArray.shape[0]
    height = numArray.shape[1]

    # Change Each Pixel to Target Color
    for row in range(width):
        for column in range(height):
            #print(numArray[row, column])
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

