import glob
import os
import cv2

inpath = "./datasets/cloth/"
outpath = "./datasets/mask/"

for file in os.listdir(inpath):
    if file.endswith(".jpg"):
        img = cv2.imread(inpath + file)
        # blur
        blurred = cv2.blur(img, (20,20))
        blurred = cv2.blur(blurred, (10,10))
        # grayscale
        gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY) 
        # 1st mask
        ret,masked1 = cv2.threshold(gray,245,255,cv2.THRESH_BINARY_INV)
        # blur the mask
        mask_blurred = cv2.blur(masked1,(15,15))
        # 2nd mask
        ret,masked2 = cv2.threshold(mask_blurred,245,255,cv2.THRESH_BINARY)

        cv2.imwrite(outpath + file, masked1)

