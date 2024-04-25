#Name: Shannon Daniels-Gamory
#Email: shannon.danielsgamory81@myhunter.cuny.edu
#Date: September 11, 2023
#This program draws a tilted square.

import turtle
a = turtle.Screen()
t = turtle.Turtle()
for i in range(5,301,5):
  t.forward(i)
  t.left(91)
  
a.exitonclick()