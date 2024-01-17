import math
import random

from PIL import Image, ImageDraw, ImageFont

profile_image = Image.open('Headshot.jpg')
WIDTH, HEIGHT = profile_image.size
ONE_ZERO_SIZE = 8

font = ImageFont.truetype('Britanic.ttf', ONE_ZERO_SIZE)
cell_width, cell_height = ONE_ZERO_SIZE, ONE_ZERO_SIZE

profile_image = profile_image.resize((int(WIDTH/cell_width), int(HEIGHT/cell_height)), Image.NEAREST)
new_width, new_height = profile_image.size
profile_image = profile_image.load()
# Create a new image with the same dimensions of the original, but all black
cyber_profile = Image.new('RGB', (WIDTH, HEIGHT), (0, 0, 0))
d = ImageDraw.Draw(cyber_profile)

for height in range(new_height):
    for width in range(new_width):
        if width % 2 == 0: continue
        r, g, b = profile_image[width, height]
        k = int((r + g + b) / 3)
        if g % 50 > 25:
            g = int(math.ceil(g / 50.0)) * 50
        else:
            g = int(math.floor(g / 50.0)) * 50
        if k < 128:
            text = "1"
        else:
            text = "0"
        d.text((width * cell_width, height * cell_height), text=text, font=font, fill=(0, g, 0))

cyber_profile.show()
cyber_profile.save('Cyber_Profile.jpg')



