import cv2
import os
import glob
import image_slicer
import matplotlib.pyplot as plt
"""
#if os.path.exists("turnel") is False:
#    os.mkdir("turnel")

#dir = sorted(glob.glob('C:/Users/masyi/Documents/eye(training)/6-turnel_vission/*'))

#image = cv2.imread('C:/Users/masyi/Documents/eye(training)/1-central_scotoma/central (1).jpg')

#brightness_4
# Improting Image class from PIL module 
from PIL import Image 

dir = sorted(glob.glob('C:/Users/masyi/Documents/eye(training)/6-turnel_vission/*'))

for path in dir:  
# Opens a image in RGB mode 
    im = Image.open(path) 
  
# Size of the image in pixels (size of orginal image) 
# (This is not mandatory) 
    width, height = im.size 
    print(width)
    print(height)
    if width == 1280:
# Setting the points for cropped image 
        left = 100
        top = 50
        right = 1200
        bottom = 630
  
# Cropped image of above dimension 
# (It will not change orginal image) 
        im1 = im.crop((left, top, right, bottom)) 
  
# Shows the image in image viewer 
        im1.show()
        data = image_slicer.slice(im1, 2, save = False)
        name = 'C:/Users/masyi/Documents/turnel/' + str(count) + '.jpg'
        image_slicer.save_tiles(data, name) 
    else:
        #print('ok')
        #data = image_slicer.slice(im, 2, save = False)
        #name = 'C:/Users/masyi/Documents/turnel/' + str(count) + '.jpg'
        #image_slicer.save_tiles(data, name)

"""
import numpy as np
import cv2

#dir = sorted(glob.glob('C:/Users/masyi/Documents/eye(training)/6-turnel_vission/*'))

#count = 0
#for path in dir:
image = cv2.imread('C:/Users/masyi/Documents/eye(training)/1-central_scotoma/central (1).jpg')
y=200
x=300
h=300
w=600
crop = image[y:y+h, x:x+w]
cv2.imshow('Image', crop) 
cv2.waitKey(0)
data = image_slicer.slice(crop, 2, save = False)
name = 'C:/Users/masyi/Documents/turnel/' + str(count) + '.jpg'
image_slicer.save_tiles(data, name)
