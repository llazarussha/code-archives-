#Name: Shannon Montana Daniels-Gamory
#Date: October 31, 2023
#This program prints time and greetings.

hour = int(input("Enter the hour of the day (0-23): "))

if 0 <= hour < 12:
    print("Good Morning")
elif 12 <= hour < 17:
    print("Good Afternoon")
else:
    print("Good Evening")
