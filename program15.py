#Name: Shannon Montana Daniels-Gamory
#Email: shannon.danielsgamory81@myhunter.cuny.edu
#Date: September 26, 2023
#This program prints a message in reverse and prints each character twice.

message = input("Enter a message:")
reversed_message = message[::-1]
for char in reversed_message:
  print(char + ' ' + char)