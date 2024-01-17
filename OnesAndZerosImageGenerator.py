import math
import random

from PIL import Image, ImageDraw, ImageFont

profile_image = Image.open('Headshot.jpg')
IMAGE_WIDTH, IMAGE_HEIGHT = profile_image.size
ONE_ZERO_SIZE = 8

font = ImageFont.truetype('Britanic.ttf', ONE_ZERO_SIZE)
cell_width, cell_height = ONE_ZERO_SIZE, ONE_ZERO_SIZE

profile_image = profile_image.resize((int(IMAGE_WIDTH/cell_width), int(IMAGE_HEIGHT/cell_height)), Image.NEAREST)
new_width, new_height = profile_image.size
profile_image = profile_image.load()
# Create a new image with the same dimensions of the original, but all black
cyber_profile = Image.new('RGB', (IMAGE_WIDTH, IMAGE_HEIGHT), (0, 0, 0))
draw = ImageDraw.Draw(cyber_profile)

for height in range(new_height):
    for width in range(new_width):
        redValue, greenValue, blueValue = profile_image[width, height]
        cellAverageIntensity = int((redValue + greenValue + blueValue) / 3)
        if greenValue % 50 > 25:
            greenValue = int(math.ceil(greenValue / 50.0)) * 50
        else:
            greenValue = int(math.floor(greenValue / 50.0)) * 50
        if cellAverageIntensity < 128:
            text = "1"
        else:
            text = "0"
        draw.text((width * cell_width, height * cell_height), text=text, font=font, fill=(0, greenValue, 0))

cyber_profile.show()
cyber_profile.save('Cyber_Profile.jpg')



