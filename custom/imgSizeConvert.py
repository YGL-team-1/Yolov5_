from PIL import Image
from glob import glob

source = "../custom_data/light_dataset/images/val/"
dst = "../custom_data/light_dataset2/images/val/"
imgs = glob(source + "*")
imgs_len = len(imgs)
count = 0
for img in imgs:
    count += 1
    if count % 100 == 0:
        print(count, "/", imgs_len)
    img_resized = Image.open(img)
    temp = img.strip().strip("\n").split("\\")[1]
    img_resized = img_resized.resize((512,288))
    img_resized.save(dst+temp)
