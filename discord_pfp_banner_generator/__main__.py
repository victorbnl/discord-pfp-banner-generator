#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""Discord profiles picture & banner generator cli"""

import re
import sys
import tempfile
import requests
from PIL import Image
from .process import process

def cli():
    """Discord profiles picture & banner generator cli"""

    # If there are no args
    if len(sys.argv) < 2:
        print("Please specify an image")
        sys.exit()

    # Load the image
    arg = sys.argv[1]
    if re.match(r'(http|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])?', arg):
        fp = tempfile.TemporaryFile()
        fp.write(requests.get(arg).content)
        image = Image.open(fp)
    else:
        image = Image.open(arg)
    
    # Create the banner and the pp
    banner, pfp = process(image)

    # Save files
    banner.save("banner.png", "PNG")
    pfp.save("pfp.png", "PNG")

    # Close temporary file
    if 'fp' in locals():
        fp.close()

if __name__ == "__main__":
    cli()
