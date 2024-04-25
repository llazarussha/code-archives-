#Name: Shannon Montana Daniels-Gamory
#Date: September 29, 2023
#Email: shannon.danielsgamory81@myhunter.cuny.edu
#This program prints the number of pixels of a user inputted image.

import matplotlib.pyplot as plt
import numpy as np

ca = plt.imread(str(input('Enter name of png file:')))
countSnow = 0
t = 0.75

for i in range(ca.shape[0]):
    for j in range(ca.shape[1]):
        if (ca[i,j,0] > t) and (ca[i,j,1] > t) and (ca[i,j,2] > t):
            countSnow = countSnow + 1

print("Snow count of", countSnow)