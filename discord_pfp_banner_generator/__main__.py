#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import re
import sys
import tempfile
from math import floor

import requests
from PIL import Image

# Constants
BANNER_WIDTH, BANNER_HEIGHT = 606, 242
PFP_X, PFP_Y = 44, 164
PFP_WIDTH, PFP_HEIGHT = 161, 161

def cli():
    # If there are no args
    if len(sys.argv) < 2:
        print("Please specify an image")
        sys.exit()
    
    # Load the image
    arg = sys.argv[1]
    if re.match(r'(http|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])?', arg):
        fp = tempfile.TemporaryFile()
        fp.write(requests.get(arg).content)
        im = Image.open(fp)
    else:
        im = Image.open(arg)

    # Resize the image
    width, height = im.size
    if width/height < 606/325:
        new_width = 606
        new_height = int(new_width*height/width)
    elif width/height > 606/325:
        new_height = 325
        new_width = int(new_height*width/height)
    im = im.resize((new_width, new_height), Image.ANTIALIAS)

    # Crop the image in the center
    width, height = im.size
    new_width, new_height = BANNER_WIDTH, BANNER_HEIGHT+PFP_HEIGHT-76
    left = floor((width - new_width)/2)
    top = floor((height - new_height)/2)
    right = floor((width + new_width)/2)
    bottom = floor((height + new_height)/2)
    im = im.crop((left, top, right, bottom))

    # Create the banner and pp variables
    banner, pfp = im.copy(), im.copy()

    # Create the banner
    banner = banner.crop((0, 0, BANNER_WIDTH, BANNER_HEIGHT))
    banner.save("banner.png", "PNG")

    # Create the pfp
    pfp = pfp.crop((PFP_X, PFP_Y, PFP_X+PFP_WIDTH, PFP_Y+PFP_HEIGHT))
    pfp.save("pfp.png", "PNG")

    # Close temporary file
    if 'fp' in locals():
        fp.close()

if __name__ == "__main__":
    cli()
