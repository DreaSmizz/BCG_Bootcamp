#lists - any group of items, separated by commas, inside square brackets []
#lists are also indexed, starting with 0 and counting up
#multiple data types in the list
numbers = [1, 2, 3, 4, 5]
length = len(numbers)
print(length)
numbers.append(6)
#insert() - listname.insert(index, item)
#numbers.insert(0,7) #add an integer
#numbers.insert(3,"ten") #add a string
#numbers.insert(0,True) #add a boolean
print("this is the appended list: ", numbers)
#remove an item by index - pop()
numberReturned = numbers.pop() #removes the last item in the list and returns it, if you want to pick a specific one, put the index number
print("this is the number removed: ", numberReturned)
print("this is our updated list: ", numbers)


#combine list
list1 = [True, False, True]
list2 = ["apple", 1, True]
list3 = list1 + list2
print(list3)

#nest a list in a list
nested_list = [list1, list2] #nesting a list with brackets
print("this is our nested list ", nested_list)

numbers2 = [5,2,3,1,4]
#sort() - sorts the list in ascending order
#numbers2.sort()
#print("the sorted list of numbers is: ", numbers2)

#goal - we only want part of the list - slice the list by giving it a range (starting and the value that's one greater than were we want to stop at)
#syntax - variable[start:end] - Note: brackets and colon
print(numbers2[0:3])

#change the item in the list - overwrite the item
#syntax - variable[index] = "new value"
numbers2[3] = 9
print(numbers2)


#looping through a list using a for loop
for number in numbers2:
    print("current number: ",number)

#copy() to create a copy of the list
numbers2_copy = numbers2.copy()

#tuple - immutable, can't be changed
example_tuple = (1, "apple", 3.14, True) #can contain different data types
#sliced - syntax - variable[start:end:increment]

#slice the elements from the begining to the second element of the tuple
slice1 = example_tuple[0:]
slice2 = example_tuple[::2] #every other element

#convert the tuple to list to make a change to it - list()
example_list = list(example_tuple)

#add a new item to the list
example_list.append("new item")

#convert the list to a tuple - tuple()
example_tuple = tuple(example_list)

#Exercise 1
numbers3 = [8, 3, 7, 5, 6]
numbers3.insert(2,4)
numbers3.pop()
print(numbers3)

#Exercise 2
fruits = ("apple", "banana", "cherry")
fruit_list = list(fruits)
fruit_list.append("orange")
fruits = tuple(fruit_list)
print(fruits)

#Exercise 3
numbers4 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers4[2:5])