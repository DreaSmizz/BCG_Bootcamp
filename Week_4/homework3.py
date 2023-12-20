#########################
#Homework Assignment 1  #
#Andrea Smith           #
#Movie Night            #
#v1.0                   #
#########################

"""
User chooses movie genre.
Based on input output shows 'you chose action/thriller/comedy
"""

print("It's Movie Night")

genre = input("Choose a movie genre, acceptable choices are action|thriller|comedy: ")

if genre.lower() == "action":
    print("You chose an action movie, might I suggest Die Hard? ")
elif genre.lower() == "thriller":
    print("You chose thriller, how about Nowhere on Netflix? ")
elif genre.lower() == "comedy":
    print("Comedy eh? Good choice, check out Glass Onion: A Knives Out Mystery")
else:
    print("Pick a valid choice.")