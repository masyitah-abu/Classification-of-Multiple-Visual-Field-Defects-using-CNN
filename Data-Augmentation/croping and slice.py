from skimage import io, img_as_float
import matplotlib.pyplot as plt
import numpy as np
import glob
import os
import image_slicer
import cv2

if os.path.exists("turnel") is False:
    os.mkdir("turnel")

#dir = sorted(glob.glob('C:/Users/masyi/Documents/eye(training)/6-turnel_vission/*'))

#count = 0
#for path in dir:
#    data = image_slicer.slice(path, 2, save = False)
#    name = 'C:/Users/masyi/Documents/turnel/' + str(count) + '.jpg'
#    image_slicer.save_tiles(data, name)
#    count += 1

dir2 = sorted(glob.glob('C:/Users/masyi/Documents/turnel/*'))
savedir = "C:/Users/masyi/Documents/turnel/OK"
count = 0
for path in dir2:
    image = cv2.imread(path)

# Select all pixels almost equal to white
# (almost, because there are some edge effects in jpegs
# so the boundaries may not be exactly white)
    white = np.array([1, 1, 1])
    mask = np.abs(image - white).sum(axis=2) < 0.05

# Find the bounding box of those pixels
    coords = np.array(np.nonzero(~mask))
    top_left = np.min(coords, axis=1)
    bottom_right = np.max(coords, axis=1)

    out = image[top_left[0]:bottom_right[0],
                top_left[1]:bottom_right[1]]

    save_to= os.path.join(savedir, "counter_{:03}.jpg")
    crop.save(save_to.format(frame_num))

    #out = cv2.imread(mask)    
    plt.imshow(out)
    plt.show()
    break


    