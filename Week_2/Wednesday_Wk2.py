"""
Scene - Birthday Party for toddlers and we need cupcakes.
Goal - how many do we need
11 toddlers
each can eat 2 cupcakes
need 3 variables
print out results to read - ??? number of cupcakes needed
"""

chaps = 11
cupcakes = 2
total_cupcakes_needed = chaps * cupcakes
print(total_cupcakes_needed, "cupcakes are needed for the toddler party")
#print(chaps*cupcakes, "cupcakes are needed for the party")
      
########
## using escape to fix single quotes within strings '\' is used
motivation = 'It\'s still your mf\'n set!' 
character = 'Captain \Backslash'  #use two backslashes when you want to print a backslash
print(motivation)
print(character)

## New line - \n
ooto = "OOTO from 12/11 - 12/22 \nFind someone else to do it."
print(ooto)

#len() - length - returns the number of characters in the string - not starting with a zero index
classic = "dogs are the best"
print(len(classic))
#zero index
print(classic[2:4])

#str() - converts an argument into a string
#type() - confirms the data type
puppies = "jade black jones-smith"
puppiesString = str(puppies)
#print(type(puppies))
#print(type(puppiesString))

#.upper() - returns the string in upper case
print(puppies.upper())
apple = "doctors love apples"
print(apple.upper())

#.lower() - returns the string in lower case
doggy = "NYLA JEAN JONES-SMITH"
print(doggy.lower())

#.capitalize() - return the string capitalized, first letter only
saying = "you smell like outside"
print(saying.capitalize())

#.title() - returns the string in title case
print(puppies.title())

# exercise - create a variable with favorite movie name in lowercase and convert to title case
movie = 'goodfellas'
print(movie.title())

#formatted strings
name = "John Smith"
adjective = "amazing"
age = str(42)
greetings = f"{name} is {adjective} at {age} years of age"
print(greetings)
print(f"{name} is {adjective} at {age} years of age")

#exercise - create three variables and print it out
advice = "drink ya water"
advice2 = "don't let people stress you out"
secretToLIfe = f"{advice} and {advice2}"
print(f"The secret to a low stress life is {advice} and {advice2}")