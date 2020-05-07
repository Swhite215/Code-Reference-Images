from PIL import Image

# Get Image
im = Image.open("../simple-pixels/3x6_CARTESIAN_TEST.png");

# Convert Image to Pixel Map
pixels = im.load()

# Create Pixel Coordinate Matrix Static
count = 0

pixelColorMatrix = [[0 for i in range(im.size[0])] for j in range(im.size[1])]

# Generate a Pixel Map and Color Map
for row in range(im.size[1]):
    for column in range(im.size[0]):
        print("Row: ", row, "Column: ", column)
        pixelColorMatrix[row][column] = pixels[column, row]
        count += 1

print(pixelColorMatrix)