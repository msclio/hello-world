from PIL import Image

# Open our image
image = Image.open("Fall_trees.jpg")
image.show()

'''
Putting a 'main' function at the top of our code means that we can call
functions without scrolling all the way to the bottom of our code; once we call
the main function once, we don't have to scroll down again
'''
def main(image):
    remove_red(image)
    grayscale(image)
    black_white(image)

'''
We use a comment block at the beginning of functions so that we can explain
what the function does and what the user should know when they call it.

"remove_red" takes an image input and sets the red value of each pixel to 0,
while keeping the green and blue values the same as the original image
'''
def remove_red(image):
    # Create a blank canvas for our new image with no red
    no_red = Image.new("RGB",(image.size[0],image.size[1]),(255,255,255))

    # Goes through each pixel of our input image and sets the pixel in the same
    # position of our blank canvas to the red-removed color value
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            pixel_value = image.getpixel((i,j))
            no_red.putpixel((i,j),(0,pixel_value[1],pixel_value[2]))

    # Makes the image show up
    no_red.show()

'''
grayscale sets the red, green, and blue values of each pixel to the average of
the three, creating a black and white image
'''
def grayscale(image):
    # Create a blank canvas for our new image in grayscale
    no_color = Image.new("RGB",(image.size[0],image.size[1]),(255,255,255))

    # Goes through each pixel of our input image and sets the pixel in the same
    # position of our blank canvas to the grayscale value
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            pixel_value = image.getpixel((i,j))
            avg_color = (pixel_value[0] + pixel_value[1] + pixel_value[2])/3
            avg_color = int(avg_color)
            no_color.putpixel((i,j),(avg_color,avg_color,avg_color))

    # Makes the image show up
    no_color.show()


def black_white(image):
    bw = Image.new("RGB",(image.size[0],image.size[1]),(255,255,255))

    for i in range(image.size[0]):
        for j in range(image.size[1]):
            pixel_value = image.getpixel((i,j))
            avg_color = (pixel_value[0]+pixel_value[1]+pixel_value[2])/3
            if avg_color > 127:
                bw.putpixel((i,j),(255,255,255))
            else:
                bw.putpixel((i,j,),(0,0,0))

    # Makes the image show up
    bw.show()
    

main(image)
