#loops - repeat tasks efficiently
# for loop - when you know in advance how many times you want to loop or iterate through the code
"""
for x in reversed(range(1,16)): #reversed() - outputs in the reverse order
    print(x)
"""

#python_cohort = "abcdefghijklmnopqrstuvwxyz"

#for x in python_cohort:
#    print(x)

"""
lucky_number = input("Guess a number: ")

for x in lucky_number:
    if x == "7":
        print("You won!")
    else:
        print("Sorry you did not win!")
        """
"""
vowel_word = input("Enter a word to search for the vowel u: ")

for letter in vowel_word:
    if letter == 'u':
        print("The letter 'u' found in the word.")
        break #the loop stops instead of continuing to run
    else:
        print("There was no 'u' found in the word.")
        """

#while loop - continue to loop or repeat the block of code while the condition is true
#guess a secret number and continue to guess until the condition is true
"""
#set the secret number
secretNumber = 2
#store the user's guess
userGuess = 0
#while loop - leep prompting the user
while userGuess != secretNumber:
    userGuess = int(input("Guess a secret number between 1 and 10: "))
    if userGuess == secretNumber:
        print("Congratulations")
    else:
        print("Wrong as raisins in potato salad.  Please try again! ")
        """

number = 5

while number > 0 and number < 10: #two conditions being checked, joined with and - both of these have to be true for the code to run
    number = number + 1
    if number == 7:
        continue #skip the number and continue running the loop
    print(number)
else:
    print("Number does not meet our conditions")
