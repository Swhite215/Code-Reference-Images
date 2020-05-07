from PIL import Image

im = Image.open("../simple-pixels/1x1_WHITE.png");

# Prints Image Format, Size NxN, and Mode
print(im.format, im.size, im.mode)

# Shows an Image
im.show()