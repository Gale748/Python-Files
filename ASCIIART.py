from PIL import Image

# define a string of characters to represent the different shades of gray
# in the image. Adjust the characters to your liking.
charmap = ' .,:;irsXA253hMHGS#9B&@'

# open the image and resize it to a smaller size to improve performance
img = Image.open('input.jpg')
width, height = img.size
img = img.resize((int(width/8), int(height/8)))

# convert the image to grayscale and get the pixel data
img = img.convert('L')
pixels = list(img.getdata())

# create an ASCII art string by mapping the brightness of each pixel to
# a character in the charmap
asciiart = ''.join([charmap[int(pixel/255 * len(charmap))] for pixel in pixels])

# print the ASCII art to the console
print(asciiart)