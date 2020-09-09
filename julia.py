import numpy as np
from matplotlib import pyplot as plt
import cv2
from PIL import Image

height, width = 500, 500

r_max, r_min = i_max, i_min = 2,-2

real_points = np.linspace(r_max, r_min, height)
imag_points = np.linspace(i_max, i_min, width)
x = y = 0
imageFile = np.zeros((height,width,3), dtype=np.uint8)
c = complex(-0.4,0.6)
for re in real_points:
    y= 0
    for img in imag_points:
        z = complex(re, img)
        n=255
        while abs(z) < 2 and n>=5:
            z = z*z + c
            n-=5
        imageFile[x,y] = [n,n,n]
        y += 1
    x += 1

cv2.imwrite("Julia_set.png",imageFile)

# colors = plt.imshow(imageFile)
lum_colors = imageFile[:,:,0]
imgplot = plt.imshow(lum_colors)
imgplot.set_cmap('hot')
# plt.show()
plt.savefig('hot_julia.png')