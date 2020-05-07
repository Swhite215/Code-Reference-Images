from PIL import Image

# Get Image
im = Image.open("../simple-pixels/3x6_CARTESIAN_TEST.png");

# Convert Image to Pixel Map
pixels = im.load()

# Create Pixel Coordinate Matrix Static
count = 0

pixelCoordinateMatrix = [[0 for i in range(im.size[0])] for j in range(im.size[1])]

# THE BELOW REUSES A LIST - EACH CHANGE TO A CELL WILL CHANGE ALL LISTS WITH THE SAME POINTER
#WTFpixelCoordinateMatrix = [[0] * im.size[0]] * im.size[1]
#WTFpixelCoordinateMatrix[0][0] = 10

# Generate a Pixel Map and Color Map
for row in range(im.size[1]):
    for column in range(im.size[0]):
        print("Row: ", row, "Column: ", column)
        pixelCoordinateMatrix[row][column] = ((row, column))
        count += 1

print(pixelCoordinateMatrix)