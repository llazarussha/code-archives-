#Name: Shannon Montana Daniels-Gamory
#Date: September 29, 2023
#Email: shannon.danielsgamory81@myhunter.cuny.edu
#This program asks for user input for an amount of hours.

wkn = int(input("Enter number of hours until weekend:"))
days = int(wkn)//24
hours = int(wkn)%24

print("days:", days)
print("hours:", hours)