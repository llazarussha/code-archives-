#Name: Shannon Montana Daniels-Gamory
#Email: shannon.danielsgamory81@myhunter.cuny.edu
#Date: September 27, 2023
#This program prompts the user for an input of an image file and extracts the red and blue color channels. 


import matplotlib.pyplot as plt
import numpy as np

img1 = input('Enter name of input file:')
img0 = input('Name new file:')
img = plt.imread(img1)

img2 = img.copy()
img2[:,:,1] = 0

plt.imsave(img0, img2)

