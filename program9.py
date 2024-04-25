#Name: Shannon Daniels-Gamory
#Email: shannon.danielsgamory81@myhunter.cuny.edu
#Date: September 13, 2023
#This program takes each letter of a user inputted word and shifts the ASCII code.

word = input("Enter a message:")
codedWord = ""

for ch in word:
  offset = ord(ch) - ord('a') + 13
  wrap = offset % 26
  newChar = chr(ord('a') + wrap)
  codedWord = codedWord + newChar

print("Your word in code is:", codedWord)