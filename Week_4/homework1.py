#########################
#Homework Assignment 1  #
#Andrea Smith           #
#Cybersecurity Check    #
#v1.0                   #
#########################

"""
Ask user if they have antivirus software installed 
Based on input give answer
"""

antivirus_software = input("Do you have antivirus software installed? Please enter a Y or N: ")

if antivirus_software.upper() == "Y":
    print("Good job! ")
elif antivirus_software.upper() == "N":
    print("Please install antivirus software as soon as possible! ")
else:
    print("You didn't input a valid answer, good luck! ")

answer = input("Do you have antivirus software installed? Please enter a Y or N: ")

if answer == "Y" or "y":
    print("Good job! ")
elif answer == "N" or "n":
    print("Please install antivirus software as soon as possible! ")
else:
    print("You didn't input a valid answer, good luck! ")