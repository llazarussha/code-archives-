#Name: Shannon Daniels-Gamory
#Email: shannon.danielsgamory81@myhunter.cuny.edu
#Date: September 13, 2023
#This program displays the shades of blue.

import turtle
mont = turtle.Turtle()
mont.shape("turtle")
mont.backward(100)

for i in range(0,260,10):
  mont.forward(10)
  mont.pensize(i)
  mont.color(0,0,i)