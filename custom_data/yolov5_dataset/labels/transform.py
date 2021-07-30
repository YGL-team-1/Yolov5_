from PIL import Image
import os
from glob import glob

import PIL


img_lists = glob("images/val/*")
for img in img_lists:
    im = Image.open(img)
    im = im.resize((1024,576))
    
    im = im.convert('RGB')
    im.save("resized_images/val/"+img.split('\\')[1])