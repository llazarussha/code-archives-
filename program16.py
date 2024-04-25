#Name: Shannon Montana Daniels-Gamory
#Email: shannon.danielsgamory81@myhunter.cuny.edu
#Date: September 27, 2023
#This program prompts the user to enter a number and move a turtle. 

import turtle
var = [1,2,3,4,5]
mont = turtle.Turtle()

for i in range(5):
  var[i] = input("please enter a number:")
  mont.left(int(var[i]))
  mont.forward(100)