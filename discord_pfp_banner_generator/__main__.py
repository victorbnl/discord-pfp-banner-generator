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
PP_X, PP_Y = 44, 164
PP_WIDTH, PP_HEIGHT = 161, 161

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
    im.save("test.png", "PNG")

    # Crop the image in the center
    width, height = im.size
    new_width, new_height = BANNER_WIDTH, BANNER_HEIGHT+PP_HEIGHT-76
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
