#Name: Shannon Montana Daniels-Gamory
#Date: October 31, 2023
#This program prints names.

input_names = input("Enter a list of names (lastName, firstName; lastName, firstName; ...): ")

names_list = input_names.split('; ')

rearranged_names = []

for name in names_list:
    last_name, first_name = name.split(', ')
    rearranged_name = first_name + ' ' + last_name
    rearranged_names.append(rearranged_name)

for name in rearranged_names:
    print(name)
