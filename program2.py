#Name: Shannon Daniels-Gamory
#Email: shannon.danielsgamory81@myhunter.cuny.edu
#Date: September 10, 2023
#This program draws an octogon.

import turtle
wn = turtle.Screen()

thomasH = turtle.Turtle()
for i in range(8):
     thomasH.forward(100)
     thomasH.left(360/8)

wn.exitonclick()