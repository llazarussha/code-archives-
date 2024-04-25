#Name: Shannon Montana Daniels-Gamory
#Date: September 29. 2023
#Email: shannon.danielsgamory81@myhunter.cuny.edu
#This program takes a user iinputted string and controls a turle.

import turtle
mont = turtle.Turtle()
letters = input("Enter string:")
for ch in letters:
    if ch =='B':
        mont.backward(50)
    elif ch == 'S':
        mont.stamp()
    elif ch == 'l':
        mont.left(45)
    elif ch == 'r':
        mont.right(45)
    elif ch == 'p':
        mont.color("purple")
    elif ch == 'F':
        mont.forward(50)
    elif ch == 'L':
        mont.left(90)
    elif ch == 'R':
        mont.right(90)
    elif ch == '^':
        mont.penup()
    elif ch == 'v':
        mont.pendown()