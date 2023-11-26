import glob

import cv2
import ipympl
import matplotlib.pyplot as plt
import numpy as np
import skimage as ski

img = cv2.imread('./datasets/cloth/02783_00.jpg')

img = cv2.blur(img,(15,15))

assert img is not None, "file could not be read, check with os.path.exists()"
thresh1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
ret,img = cv2.threshold(thresh1,245,255,cv2.THRESH_BINARY_INV)
img = cv2.blur(img,(10,10))
ret,img = cv2.threshold(img,245,255,cv2.THRESH_BINARY)


cv2.imwrite("./datasets/mask/02783_00.jpg", img)