import io
import os
import json
from PIL import Image,ImageDraw,ImageFont


img = Image.open("./imgs/img001.jpg")
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf", 25)
draw.text((0, 0),"Sample Text",(0,0,0),font=font)
draw.text((0, 25),"Sample Text",(0,0,0),font=font)
img.show()
#['img011.jpg', 't shirt', 'player', 'photo caption', 'product', 'facial hair', 'font']
