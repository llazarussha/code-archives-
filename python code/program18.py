#Name: Shannon Montana Daniels-Gamory
#Email: shannon.danielsgamory81@myhunter.cuny.edu
#Date: September 29, 2023

import matplotlib.pyplot as plt 
import numpy as np

var = int(input('Enter file size:'))
img = np.ones((var,var,3))

img[::2, :,1] = 0
img[1::2, :,2] = 0

var2 = input('Enter new file name:')

plt.imsave(var2,img)


   