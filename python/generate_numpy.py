#generate_numpy.py
from PIL import Image
import numpy as np
import timeit

def generate_numpy(imgPath=None):

    if imgPath is None:
        raise Exception("Exception: A valid image path was not provided")

    img = imgPath
    
    # Get Image
    im = Image.open(img)

    # Convert Image to Numpy Array
    numArray = np.array(im)

    return numArray

    # Convert Numpy Array Back to Image
    #imageFromArray = Image.fromarray(numArray)

# Execution Time = .010
#print(timeit.timeit(generate_numpy, number=1))