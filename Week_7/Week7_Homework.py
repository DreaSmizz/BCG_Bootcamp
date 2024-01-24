##################
# Andrea Smith
# Exercise 1
# Jan 24, 2024
# v1.0
##################

"""
Create a list of five different books and use the append method to add one more book to the list.  Print the final list
"""

print("Exercise 1:")
book_list = ["Hitchhiker's Guide to the Galaxy", "A Promised Land", "The First, the Few, the Only: How Women of Color...", "1984", "Farenheit 451"]
book_list.append("A Tale of Two Cities")
print("The books in our list are: ", book_list)
print("###############")

##################
# Andrea Smith
# Exercise 2
# Jan 24, 2024
# v1.0
##################

"""
Number list containing [1,3,5,7,9] insert 2 in the first position and 4 in the third position.  Position refers to index position, print the updated list.
"""

print("Exercise 2:")
numbers = [1, 3, 5, 7, 9]
print("Numbers in our list: ", numbers)
numbers.insert(0,2)
numbers.insert(2,4)
print("Numbers in our list now: ", numbers)
print("###############")

 

##################
# Andrea Smith
# Exercise 3
# Jan 24, 2024
# v1.0
##################


"""
Create tuple eith elements (10,20,30,40,50), convert to list, remove last two elements and convert back to tuple, print final tuple
"""

print("Exercise 3:")
number_tuple = (10, 20, 30, 40, 50)
print("Numbers in our tuple is: ", number_tuple)
number_list = list(number_tuple)
number_list.pop()
number_list.pop()
number_tuple = tuple(number_list)
print("Numbers in our tuple now is: ", number_tuple)
print("###############")

 
##################
# Andrea Smith
# Exercise 4
# Jan 24, 2024
# v1.0
##################

"""
Take list of items [airway, basketball, cookies, diet, enjoy], use slicing to create a new variable that stores the items from the second to fourth elements and print it out
"""

print("Exercise 4:")
stuff = ["airway", "basketball", "cookies", "diet", "enjoy"]
print("Current items in our list: ", stuff)
new_stuff = stuff[1:4]
print("New list: ", new_stuff)
print("###############")

 

##################
# Andrea Smith
# Exercise 5
# Jan 24, 2024
# v1.0
##################

"""
Create a tuple, print second element
"""

print("Exercise 5:")
teams = ("Vikings", "49ers", "Tampa Bay", "Panthers", "Bills")
print("Teams in the tuple: ", teams)
print("The second element in the tuple is: ", teams[1])
print("###############")

##################
# Andrea Smith
# Exercise 6
# Jan 24, 2024
# v1.0
##################

"""
Create two lists where the first list contains three elements and the second list contains four elements.  Print the nested list.
"""

print("Exercise 6:")
football_teams = ["Cardinals", "Raiders", "Ravens"]
basketball_teams = ["Bulls", "Celtics", "Lakers", "Knicks"]
teams_combined = [football_teams, basketball_teams]
print("Our nested list is: ", teams_combined)
print("###############")

##################
# Andrea Smith
# Exercise 7
# Jan 24, 2024
# v1.0
##################

"""
Given a tuple (5, 10, 15, 20), convert it to a list, replace the second element with 12 and convert it back to tuple.  Print the final tuple
"""

print("Exercise 7:")
final_tuple = (5, 10, 15, 20)
final_list = list(final_tuple)
final_list[1] = 12
final_tuple = tuple(final_list)
print("Items in tuple are: ", final_tuple)
print("###############")