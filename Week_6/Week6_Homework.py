#################################
# Andrea Smith
# Problem 1 - Name and Age
# v1.0
#################################

"""
Create variable name and age.  Print message using an f-string to display the name and age.
"""
print("Exercise 1")

name = "Drea"
age = 21

print(f"Hello {name}, you are {age} years old!")

print("###############")

#################################
# Andrea Smith
# Problem 2 - Name and Age
# v1.0
#################################

"""
Create a string and use len() function to find and print its length
"""
print("Exercise 2")

quote = "Go take a bath, you smell like outside! - Black Mothers Everywhere"

print(f'The number of characters in our, quote: {quote} is,',len(quote))

print("###############")

#################################
# Andrea Smith
# Problem 3 - Odd Number Print
# v1.0
#################################

"""
Print all odd numbers from 15 to 35 using a for loop.
"""

print("Exercise 3")

for i in range(15,36,2):
    print(i)

print("###############")

#################################
# Andrea Smith
# Problem 4 - Square biz
# v1.0
#################################

"""
Print the square of numbers from 1 to 4 using a loop
"""

print("Exercise 4")

for x in range(1,5):
    print(x**2)

print("###############")

#################################
# Andrea Smith
# Problem 5 - Even number count down
# v1.0
#################################

"""
Print all even numbers from 2 to 8 using a while loop.
"""

print("Exercise 5")

count = 9
num = 2

while num < count:
    print(num)
    num += 2
print("###############")

#################################
# Andrea Smith
# Problem 6 - Print the sum
# v1.0
#################################

"""
Calculate the sum of numbers from 1 to 5 using a while loop.
"""    

print("Exercise 6")

sum_num = 0
count = 0
    
while count <= 5:
    sum_num = count + sum_num
    count += 1
print(sum_num)
     
print("###############")

#################################
# Andrea Smith
# Problem 7 - Colors
# v1.0
#################################

"""
Create an empty list named colors.  Append three different colors to the list.
"""    

print("Exercise 7")

colors = []
#count = 0
#num_colors = int(input("How many colors do you want to enter? "))
color = input("Enter a color, enter quit when done ")


while color != "quit":
    colors.append(color)
    color = input("Enter a color, enter quit when done ")

print(f"You entered the following colors: {colors}")    
print("###############")

#################################
# Andrea Smith
# Problem 8 - Colors again
# v1.0
#################################

"""
Remove one color from the list created in problem 7.
"""    

print("Exercise 8")

answer = input(f"These are the colors in your list, {colors}, would you like to remove one?  Enter 'y' or 'n'. ")

if answer.lower() == "y":
    for color in colors:
        colors.remove(color)
        answer = input(f"These are the colors in your list, {colors}, would you like to remove one?  Enter 'y' or 'n'.")

print(f"These are the colors left in your list, {colors}")
    
print("###############")

#################################
# Andrea Smith
# Problem 9 - Guess game
# v1.0
#################################

"""
Create a guessing game that takes a user input for their age and print a message with their age while using a while loop.
"""    

print("Exercise 9")
print("Let's play a game. I'm going to guess your age.")
age = int(input("Enter your age: "))






print("###############")

#################################
# Andrea Smith
# Problem 10 - Two numbers
# v1.0
#################################

"""
Take user input for two numbers, convert them to integers, and print their sum.
"""    

print("Exercise 10")

num1 = int(input("Please enter your first number: "))
num2 = int(input("Please enter your second number: "))

print(f"The sum of your two numbers is,", num1 + num2)

print("###############")