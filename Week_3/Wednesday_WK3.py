#input() - receives a value from the user and stores it in the variable
lucky = int(input("Enter your lucky Number: "))
print(f'Your lucky number is: {lucky}')
print(type(lucky))

"""
Create a statement that takes in a value and saves it in a variable.
Then use the f string method to print out the value
Convert the value into an integer using the int method
"""

number_of_pets = int(input("How many pets do you have: "))
print(f'You have {number_of_pets} pets.')
print(type(number_of_pets))

#Exercise - Simple Calculator
#Print out the sum of two numbers received from a user and use a f-string

num1 = float(input('Enter the first number: '))
num2 = float(input('Enter the second number: '))

#Operations
answer = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2

#Output for user
print(f'The sum of {num1} and {num2} is {answer}.')
print(f'The difference of {num1} and {num2} is {difference}.')
print(f'The product of {num1} and {num2} is {product}.')
print(f'The quotient of {num1} and {num2} is {quotient}.')


#Exercise - strings using input() and len() and f-string
#generate a greeting that says hello to the user and advises the length of characters in the name.
#num_of_characters = len(name)
#print(f'Hello {name}! Nice to meet you, your name has {num_of_characters} in it')

name = input('What is your name? ')
print(f'Hello {name}! Nice to meet you, your name has', len(name), 'in it')


#Exercise - temperature conversion
celsuis = float(input('Enter temperature in Celsuis: '))
fahrenheit = (celsuis * 9/5) + 32

#display result
print(f'{celsuis} degrees Celsuis is equal to {fahrenheit} degrees in Fahrenheit')