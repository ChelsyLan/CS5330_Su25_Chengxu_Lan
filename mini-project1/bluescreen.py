"""
File: bluescreen.py
--------------------
This program shows an example of "greenscreening" (actually
"bluescreening" in this case).  This is where we replace the
pixels of a certain color intensity in a particular channel
(here, we use blue) with the pixels from another image.
"""

from simpleimage import SimpleImage


INTENSITY_THRESHOLD = 1.1


def bluescreen(main_filename, back_filename):
    """
    Implements the notion of "bluescreening".  That is,
    the image in the main_filename has its "sufficiently blue"
    pixels replaced with pixel from the corresponding x,y
    location in the image in the file back_filename.
    Returns the resulting "bluescreened" image.
    """
    image = SimpleImage(main_filename)
    back = SimpleImage(back_filename)

    # See if this pixel is "sufficiently" blue
    # If so, we get the corresponding pixel from the
    # back image and overwrite the pixel in
    # the main image with that from the back image.
    # Add your code hear
    width = image.width
    height = image.height
    # new_image = SimpleImage()

    for x in range(width):
        for y in range(height):
            pixel = image.get_pixel(x,y)
            if pixel.blue > pixel.red * INTENSITY_THRESHOLD and pixel.blue > pixel.green * INTENSITY_THRESHOLD:
                new_pixel = back.get_pixel(x,y)
                image.set_pixel(x,y,new_pixel)
               

    return image


def main():
    """
    Run your desired image manipulation functions here.
    You should store the return value (image) and then
    call .show() to visualize the output of your program.
    """
    original_stop = SimpleImage('stop.png')
    # original_stop.show()

    original_leaves = SimpleImage('leaves.png')
    # original_leaves.show()

    stop_leaves_replaced = bluescreen('stop.png', 'leaves.png')
    stop_leaves_replaced.show()


if __name__ == '__main__':
    main()
