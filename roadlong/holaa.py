print("The start of the way")
# an expression is a piece of code that produces a value
print(10 * "x")

#variables
"""
python executes the code line by lane
Python is a key sensitive language which means it's sensitive to
lower case and upper case letters.
"""

# full_name = 'John Smith'
# age = 20
# is_new = True
# name = input("What is you name?")
# print(f"Hi {name}")

# name = input("What is your name? ")
# print("Hi " + name

# person = input("What is your name? ")
# color = input("What is your favourite colour? ")
# print(person + " likes " + color)

# msg = "Hey ce faci?"
# eu = "Am primit mesajul :"
# primit = f"{eu}'{msg}' de la o fata"
# print(primit)

# formated string

#format strings
# first = "John"
# last = "Smith"
# message = first + " [" + last + "] is a coder"
# print(message)
# msg = f"{first} [{last}] is a coder"
# print(msg)

#string methods
course = "Python for Beginners"
print(len(course))
# len is a general purpose function
print(course.upper())
print(course.find("o"))
# the method find is case sensitive,
"""
To verify the existence of your sring, value etc ...in that situations we use the in operator which returns a
boolean value

What is the difference between functions and methods?

"""
print(course.replace("Beginners", "LiL Beginners"))

""" Arithmetic Operations """
"""
/ division it gives out a floating value 3.333335
or 
// gives the result in a integer value
% returns what remains after the division
** power, 10 ** 3, ten to the power of three
x = x + 3 can be written as x += 3 and can be called an AUGMENTED ASSIGNMENT OPERATOR
"""

""" OPERATOR PRECEDENCE """
""" BASIC MATH CONCEPT, 0. parenthesis
first we have exponentiation: 2**2,
second multiplication or division
third we have addition or substraction
"""

""" IF STATEMENTS"""

# house_price = 1000000
# good_credit = False
#
# if good_credit:
#     print("Buyer has a good credit")
#     print(f"{int(house_price/10)}")
# else:
#     print("Buyer doesn't have a good creidt")
#     house_price /= 20
#     print(int(house_price))


# weight = input("Weight: ")
# unit = input("(L)bs or (K)g: ")
# if unit == "L" or unit == "l":
#     print(f"Your weight is {(int(weight))*0.45} Lbs")
# else:
#     weight = int(weight) / 0.45
#     print(f"Your weight is {weight} kg")
#
""" While loops"""
# index = 1
# while index <= 5:
#     print(index)
#     index = index + 1
# print("Done")


# CAR GAME

# while True:
#     command = input(">").lower()
#     if command == "help":
#         print("""
# start - to start the car
# stop - to stop the car
# quit - to quit the car
#         """)
#     elif command == "start":
#         print("Car started...")
#     elif command == "stop":
#         print("Car has stopped...")
#     elif command == "quit":
#         break
#     else:
#         print("I don't understand")

# started = False
# while True:
#     command = input(">").lower()
#     if command == "help":
#         print("""
# start - to start the car
# stop - to stop the car
# quit - to quit the car
#         """)
#     elif command == "start":
#         if started:
#             print("Car is already started")
#         else:
#             started = True
#             print("Car started...")
#
#     elif command == "stop":
#         if not started:
#             print("Car is stopped already")
#         else:
#             started = False
#             print("Car has stopped...")
#     elif command == "quit":
#         break
#     else:
#         print("I don't understand")


""" For loop """
# for item in "Python":
#     print(item)
#
# for item in ["Mos", "Power", "Achile"]:
#     print(item)
#
# prices = [10, 20 , 30]
# sum = prices[0] + prices[1] + prices[2]
# for itemo in prices:
#     print(sum)
#     break
#
# prices = [10, 20, 30]
# total = 0
# for price in prices:
#     total += price
# print(f"Total: {total}")

"""Nested Loops"""
"""Using a nested loop means adding one loop inside another loop--we can easily generate coordinates, like (x,y)"""

# for x in range(4):
#     for y in range(3):
#         print(f"({x}, {y})")
#

# exercise

numbers = [5, 2, 5, 2, 2]

for x_count in numbers:
    output = ""
    for count in range(x_count):
        output += "x"
    print(output)

""" 
List
"""

names = ["Jhon" , "Bob", "Mosh", "Sarah", "Mara"]

numbers = [1, 2, 3, 20, 40, 500, 1200]
maxi = numbers[0]
for number in numbers:
    if number > maxi:
        maxi = number
print(maxi)

maximum = max(numbers)
for number in numbers:
    print(maximum)
    break

"""2D list-data science and machine learning"""
""" matrix """

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# how do we acces 1 from the list which is inside of another list?
matrix[0] # this returns the first list
matrix[0][0]
print(matrix[0][0])

for row in matrix:
    for item in row:
        print(item)

"""List methods"""

numbers = [5, 2, 1, 7, 4]
numbers.append(13)
print(numbers)

"""insert - it takes two values"""
numbers.insert(0, 10)
print(numbers)
numbers.remove(5)
print(numbers)

""" pop - remove the last number from a list = numbers.pop()"""
# numbers.index(5) # shows the first occurence of the first number
print(50 in numbers) # safer than index cuz it doesn;t return error
""" count - returns the number of elements counted in the list/dictionary"""

numbers.sort()
numbers.reverse()
print(numbers)

numbers2 = numbers.copy()
numbers.append(9)
print(numbers2)
# they are independent

"""remove the duplicates from a list"""

list1 = [1, 3, 4, 3, 5, 9, 1]
uniques = []
for numbers in list1:
    if numbers not in uniques:
        uniques.append(numbers)
print(uniques)

"""tuples - we can't modify them, they are immutable"""

numbers = (1, 2 ,3)

"""unpacking"""
coordinates = (1, 2 ,3)
# coordinates[0] * coordinates[1] * coordinates [2]   # not good
# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]

x, y, z = coordinates # same as the upper
print(x)
print(y)
"""we can use this feature to list as well"""

"""Dictionary - we want to store information that comes as key value pairs"""
""" think like a customer, he has name, email, phone etc---a bunch of atributes
each of this atribute has a value
name, email - key
John, aweaeawe@yahoo.com  are values
"""

customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
# each key should be unique!!!
print(customer["name"]) #key sensitive, shows error if we write with upper or don;t find the value
print(customer.get("NAME"))
customer["birthdate"] = "Jan 1 1980"
print(customer)

phone = input("Phone:")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six"
}
output = ""
for character in phone:
    output += digits_mapping.get(character, "!") + " "
print(output)

