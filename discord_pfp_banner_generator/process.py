"""Creates the banner and the profile picture"""

import os
import sys
from math import floor

import yaml
from PIL.Image import ANTIALIAS

# Get the positions
with open(os.path.join(sys.path[0], "positions.yml"), "r") as f:
    positions = yaml.safe_load(f.read())

def process(image):
    """Creates the banner and the profile picture from the given image as banner.png and pfp.jpg"""

    # Resize the image
    width, height = image.size
    # If the image is taller than the desired one
    if width/height < positions["output"]["w"]/positions["output"]["h"]:
        new_width = positions["output"]["w"] # We want to have the correct width
        new_height = int(new_width*height/width) # And adjust the height to keep the ratio
    # If the image is larger than the desired one
    elif width/height > positions["output"]["w"]/positions["output"]["h"]:
        new_height = positions["output"]["h"] # We want to have the correct height
        new_width = int(new_height*width/height) # And adjust the width to keep the ratio
    # Finally, resize the image
    image = image.resize((new_width, new_height), ANTIALIAS)

    # Crop the image in the center
    width, height = image.size
    new_width = positions["output"]["w"]
    new_height = positions["output"]["h"]
    image = image.crop(
        (
            floor((width - new_width)/2),   # left
            floor((height - new_height)/2), # top
            floor((width + new_width)/2),   # right
            floor((height + new_height)/2)  # bottom
        )
    )

    # Create the banner and pfp variables
    banner, pfp = image.copy(), image.copy()

    # Create the banner
    banner = banner.crop(
        (
            0,                        # x
            0,                        # y
            positions["banner"]["w"], # x_
            positions["banner"]["h"]  # y_
        )
    )

    # Create the pfp
    pfp = pfp.crop(
        (
            positions["profile-picture"]["x"],                                   # x
            positions["profile-picture"]["y"],                                   # y
            positions["profile-picture"]["x"]+positions["profile-picture"]["w"], # x_ (x + width)
            positions["profile-picture"]["y"]+positions["profile-picture"]["h"]  # y_ (y + height)
        )
    )

    return banner, pfp
