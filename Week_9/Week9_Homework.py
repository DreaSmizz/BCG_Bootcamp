##################
# Andrea Smith
# Exercise 1
# Feb 17, 2024
# v1.0
##################

"""
Create dictionary representing student's grades(values) with subjects(keys), print all the subjects.  Ensure dictionary has at least 4 grades and subjects
"""

print("Exercise 1:")
students = {"Language Arts": "A", "Math": "B", "Science": "A", "Art": "A"}
print("Keys", list(students.keys()))
print("###############")


##################
# Andrea Smith
# Exercise 2
# Feb 17, 2024
# v1.0
##################

"""
Create dictionary representing a player(key) and favorite dish (value), print all the dishes(values).
"""
print("Exercise 2:")
favorite_dishes ={"Drea": "Steak", "Zoe": "Pizza", "Paris": "Bread", "Rissa": "Seafood"}
print("Values", list(favorite_dishes.values()))
print("###############")

##################
# Andrea Smith
# Exercise 3
# Feb 17, 2024
# v1.0
##################

"""
Find the index of a specific character in a string.  Print the index of a letter.  Create own string.
"""

print("Exercise 3:")
phrase = "Python is cool!"
result = phrase.index('i')
print(result)
print("###############")

##################
# Andrea Smith
# Exercise 4
# Feb 17, 2024
# v1.0
##################

"""
Create a dictionary of your choosing and convert to uppercase.
"""

print("Exercise 4:")
cars = {"suv": "jeep", "truck": "dodge", "sports car": "mustang", "luxery": "mercedes"}
new_cars = {k.upper():v.upper() for k,v in cars.items()}
print(new_cars)
print("###############")


##################
# Andrea Smith
# Exercise 5
# Feb 17, 2024
# v1.0
##################

"""
Remove and return the last key/value pair from a dictionary
"""

print("Exercise 5:")
print("###############")