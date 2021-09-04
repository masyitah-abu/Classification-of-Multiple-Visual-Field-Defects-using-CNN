import cv2
import numpy
import os
import glob

from PIL import Image
from PIL import ImageCms

# force opening truncated/corrupt image files
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

if os.path.exists("quadratopia") is False:
    os.mkdir("quadratopia")

dir = sorted(glob.glob('C:/Users/masyi/Documents/eye_train/quadratopia/*'))

count = 0
for path in dir:
    img = cv2.imread(path)
## (1) Convert to gray, and threshold
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    th, threshed = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)

## (2) Morph-op to remove noise
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11,11))
    morphed = cv2.morphologyEx(threshed, cv2.MORPH_CLOSE, kernel)

## (3) Find the max-area contour
    cnts = cv2.findContours(morphed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    cnt = sorted(cnts, key=cv2.contourArea)[-1]

## (4) Crop and save it
    x,y,w,h = cv2.boundingRect(cnt)
    dst = img[y:y+h, x:x+w]
    dst = cv2.resize(dst, (224,224))

    name = 'C:/Users/masyi/Documents/quadratopia/' + str(count) + '.jpg'

    #cv2.imshow("image", dst)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    cv2.imwrite(name, dst)
    count += 1
