from glob import glob
import cv2
import numpy as np
from PIL import Image

imgs = glob("custom_data/light_dataset2/images/train/*")
count = 0
for im in imgs:
    count += 1
    if count < 8230:
        continue
    img = cv2.imread(im)
    
    # img Brightness Convert
    pixel_avg = [-0.8*i for i in cv2.mean(img)]
    pixel_avg = np.array(pixel_avg)
    BCimg = cv2.add(img, pixel_avg)
    cv2.imshow("BCimg", BCimg)

    # Color img Normalize
    Normalized_img = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
    Normalized_img[:,:,0] = cv2.equalizeHist(Normalized_img[:,:,0])
    Normalized_img = cv2.cvtColor(Normalized_img, cv2.COLOR_YUV2BGR)
    cv2.imshow("Normalized_img",Normalized_img)

    # Canny edge
    edge_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_mean = cv2.mean(edge_img)
    edge_img = cv2.Canny(edge_img,0, 255) #  round(img_mean[0] * 0.2 , 0)
    cv2.imshow("edge_img", edge_img)

    # laplacian
    laplacian_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    laplacian_img = cv2.Laplacian(laplacian_img, -1)
    cv2.imshow("laplacian_img",laplacian_img)


    cv2.imshow("img", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()