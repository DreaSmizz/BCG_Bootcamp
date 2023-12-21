#Conditional statements - if, else, elif

#if - only executes a block of code if the condition is true
#else - only executes a block of code if another action or decision because the if statement proved false
#elif - else if - this precedes the else statement

"""
age = int(input("Please enter you age: "))

if age < 18:
    print("You can't vote yet") #indentation - recommendation is 4 spaces
elif age == 18:
    print("You are 18, you can vote, CONGRATS.")
else:
    print("You are able to vote")
"""

#logical operators - and, or, not
# 'and' operator - both statements have to be true
# 'or' operator - either statement has to be true
# 'not' operator - evaluates to ensure it is false

age = 25
income = 5000

#older than 18 and income over 30000
if age > 18 and income > 30000:
    print("You are eligible for a loan")