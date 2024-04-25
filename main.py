#Name: Shannon Montana Daniels-Gamory
#Email: shannon.danielsgamory81@myhunter.cuny.edu
#Date: September 27, 2023
#This program translates pseudocode into a program

s = input("Enter a string:")
ls = len(s)
for i in range(ls):
  print(s[:i])
  
  for i in range(ls):
    print(s[i:])

print("Program completed.")