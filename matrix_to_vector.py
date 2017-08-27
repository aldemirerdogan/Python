# import libraries for image acquisition
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Load an color image in grayscale d
img = mpimg.imread('tulip.jpg')

# plot the data in RGB
image_plot = plt.imshow(img)

# Select a color from RGB
lum_img = img[:, :, 2]

# Plot the blue matrix
image_plot_2 = plt.imshow(lum_img)
