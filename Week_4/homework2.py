#########################
#Homework Assignment 1  #
#Andrea Smith           #
#Family Outing          #
#v1.0                   #
#########################

"""
Ask user if they prefer a park, museum or movie using input()
"""

print("Family Outing")

outing = input("Would you like to go to the Park, Museum or Movie? ")

if outing.title() == "Park":
    print("Let's enjoy a day outdoors! ")
elif outing.title() == "Museum":
    print("Get ready for a cultural experience! ")
elif outing.title() == "Movie":
    print("Movie night it is, good luck agreeing on a selection! ")
else:
    print("Please input a valid selection! ")