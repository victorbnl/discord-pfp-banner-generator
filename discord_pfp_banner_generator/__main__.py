#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# Imports
from PIL import Image
import sys
from math import floor

# Constants
BANNER_WIDTH, BANNER_HEIGHT = 606, 242
PP_X, PP_Y = 44, 164
PP_WIDTH, PP_HEIGHT = 161, 161

def cli():
    # Load the input image
    im = Image.open(sys.argv[1])

    # Check if it's landscape
    width, height = im.size
    if height > width:
        print("Please use a landscape image")
        sys.exit()

    # Resize the image to 600px width
    im.thumbnail((BANNER_WIDTH, BANNER_WIDTH), Image.ANTIALIAS)

    # Crop the image in the center
    width, height = im.size
    new_width, new_height = width, BANNER_HEIGHT+PP_HEIGHT-76
    left = floor((width - new_width)/2)
    top = floor((height - new_height)/2)
    right = floor((width + new_width)/2)
    bottom = floor((height + new_height)/2)
    im = im.crop((left, top, right, bottom))

    # Create the banner and pp variables
    banner, pp = im.copy(), im.copy()

    # Create the banner
    banner = banner.crop((0, 0, BANNER_WIDTH, BANNER_HEIGHT))
    banner.save("banner.png", "PNG")

    # Create the pp
    pp = pp.crop((PP_X, PP_Y, PP_X+PP_WIDTH, PP_Y+PP_HEIGHT))
    pp.save("pp.png", "PNG")

if __name__ == "__main__":
    cli()
