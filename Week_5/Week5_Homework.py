##################
# Andrea Smith
# Exercise 1
# Jan 9, 2024
# v1.0
##################

"""
Write a program using a 'for' loop to print the numbers 1 to 5.
"""

for i in range(1,6):
    print(i)

##################
# Andrea Smith
# Exercise 2
# Jan 9, 2024
# v1.0
##################

"""
Write a program using a 'while' loop to countdown from 5 to 1.
"""

count = 5

while count != 0:
    print(count)
    count -= 1

 
##################
# Andrea Smith
# Exercise 3
# Jan 9, 2024
# v1.0
##################


"""
Create a guessing game using a 'while' loop where the user guesses a secret number that you have chosen
"""

secret_num = 7

guess = int(input("Guess a number between 1 and 10: "))

while secret_num != guess:
    print("Ah Ah Ah guess again!")
    guess = int(input("Guess a number between 1 and 10: "))

 
##################
# Andrea Smith
# Exercise 4
# Jan 9, 2024
# v1.0
##################

"""
Use a 'for' loop to print all even numbers between 1 and 10.  Remember: for i in range(1,2,3)
"""

for i in range(2,11,2):
    print(i)


##################
# Andrea Smith
# Exercise 5
# Jan 9, 2024
# v1.0
##################

"""
Create a program that repeatedly asks the user for a password until the enter the correct one using a while loop
"""

password = "friday"
user_guess = input("What's the password? ")

while user_guess.lower() != password:
    print("Try again!")
    user_guess = input("What's the password? ")

##################
# Andrea Smith
# Exercise 6
# Jan 9, 2024
# v1.0
##################


"""
Create a program that asks the user to enter the word 'quit' to exit a pgoram.  Once 'quit' is entered print out a response saying 'Goodbye'
"""

magic_word = "quit"

user = input("Gotcha going in circles......enter the right word to leave! ")

while user.lower() != magic_word:
    print("Nope, try again! ")
    user = input("Gotcha going in circles......enter the right word to leave! ")
    print("Goodbye!")