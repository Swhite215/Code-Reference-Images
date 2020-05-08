from PIL import Image
import numpy as np
import timeit

def generate_numpy():
    # Get Image
    im = Image.open("../simple-pixels/3x6_CARTESIAN_TEST.png")

    # Convert Image to Numpy Array
    numArray = np.array(im)

    print(numArray)

    # Convert Numpy Array Back to Image
    imageFromArray = Image.fromarray(numArray)

    print(imageFromArray)

# Execution Time = .010
print(timeit.timeit(generate_numpy, number=1))