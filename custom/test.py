import cv2
from glob import glob
import numpy as np

imgs = glob("custom_data/light_dataset2/images/train/*")
count = 0

for im in imgs:
    img = cv2.imread(im, cv2.IMREAD_COLOR)
    
    data = img.copy()
    y, x, dim = data.shape
    
    data = data.flatten()
    avg = np.mean(data)
    converted_data = [ i if i < avg*2 else i-avg for i in data]
    converted_data = np.reshape(converted_data,(y,x,dim))

    cv2.imshow("img", converted_data)
    if cv2.waitKey(100) == 27:
        break

cv2.destroyAllWindows()