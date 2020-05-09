from PIL import Image
import numpy as np
import timeit
import sys


def complex_pixel_alter_twoColors():
        oldImagePath = "../complex-pixels/ECRIC_UNCOLORIZED.png"
        newImagePath = "../new-images/ECRIC_COLOR_ATTEMPT_1.png"

        im = Image.open(oldImagePath)

        print(im.format, im.size, im.mode)

        pixels = im.load()

        # Show Current Image
        im.show()

        # Important Values
        backgroundColorTuple = (255, 255, 255, 255)
        earthColorTuple = (228, 228, 228, 255)
        newBackgroundColorTuple = (25, 25, 25, 255)
        newEarthColorTuple = (255, 255, 255, 255)

        # First Change Background Color
        for i in range(im.size[0]):
                for j in range(im.size[1]):
                        if pixels[i,j] == (255, 255, 255, 255):
                                pixels[i,j] = newBackgroundColorTuple

        # Generate Differences List
        remainingColors = []
        for i in range(im.size[0]):
                for j in range(im.size[1]):
                        if pixels[i,j] != newBackgroundColorTuple:
                                if pixels[i,j] not in remainingColors:
                                        remainingColors.append(pixels[i,j])

        im.show()
        sys.exit()

        # Change Remaining to Single Color
        for i in range(im.size[0]):
                for j in range(im.size[1]):
                        if pixels[i,j] in remainingColors and pixels[i,j] != newBackgroundColorTuple:
                                pixels[i,j] = (255, 255, 255, 255)

        #Show Altered Image
        im.show()

        # Save Image
        im.save(newImagePath)

# Execution Time 1.38
print(timeit.timeit(complex_pixel_alter_twoColors, number=1))