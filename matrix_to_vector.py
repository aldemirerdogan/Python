import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

# Load an color image in grayscale d
img = mpimg.imread('lena.jpg')
imgplot = plt.imshow(img)
plt.imshow(imgplot)