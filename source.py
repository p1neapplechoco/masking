import glob
import os
import cv2

def change_brightness(img, value=30):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    v = cv2.add(v,value)
    v[v > 255] = 255
    v[v < 0] = 0
    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img


inpath = "./datasets/cloth/"
outpath = "./datasets/mask/"

for file in os.listdir(inpath):
    if file.endswith(".jpg"):
        img = cv2.imread(inpath + file)
        # blur
        blurred = cv2.blur(img, (15,15))
        # grayscale
        gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY) 
        # 1st mask
        ret,masked1 = cv2.threshold(gray,245,255,cv2.THRESH_BINARY_INV)
        # blur the mask
        mask_blurred = cv2.blur(masked1,(10,10))
        # 2nd mask
        ret,masked2 = cv2.threshold(mask_blurred,245,255,cv2.THRESH_BINARY)

        cv2.imwrite(outpath + file, masked1)

