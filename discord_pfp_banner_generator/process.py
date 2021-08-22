"""Creates the banner and the profile picture"""

from math import floor
from PIL.Image import ANTIALIAS

# Constants
BANNER_WIDTH, BANNER_HEIGHT = 606, 242
PFP_X, PFP_Y = 44, 164
PFP_WIDTH, PFP_HEIGHT = 161, 161

def process(image):
    """Creates the banner and the profile picture from the given image as banner.png and pfp.jpg"""

    # Resize the image
    width, height = image.size
    if width/height < 606/325:
        new_width = 606
        new_height = int(new_width*height/width)
    elif width/height > 606/325:
        new_height = 325
        new_width = int(new_height*width/height)
    image = image.resize((new_width, new_height), ANTIALIAS)

    # Crop the image in the center
    width, height = image.size
    new_width, new_height = BANNER_WIDTH, BANNER_HEIGHT+PFP_HEIGHT-76
    left = floor((width - new_width)/2)
    top = floor((height - new_height)/2)
    right = floor((width + new_width)/2)
    bottom = floor((height + new_height)/2)
    image = image.crop((left, top, right, bottom))

    # Create the banner and pp variables
    banner, pfp = image.copy(), image.copy()

    # Create the banner
    banner = banner.crop((0, 0, BANNER_WIDTH, BANNER_HEIGHT))

    # Create the pfp
    pfp = pfp.crop((PFP_X, PFP_Y, PFP_X+PFP_WIDTH, PFP_Y+PFP_HEIGHT))

    return banner, pfp
