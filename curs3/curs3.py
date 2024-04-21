month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# def is_leap(year):
#     if year % 4 == 0 and (year % 100 == 0 or year % 400 == 0):
#         return
#
# def days_in_month(year, month):
#     if not 1 <= month <= 12:
#         return 'Invalid month'
#     if month == 2 and is_leap(year):
#         return 29
#     return month_days[month]


#write a program that will display whether the value of the variable is divisible by 7

# n = int(input("Please select a number = "))
# while n % 7 == 0:
#     print(f"The selected value {n} is divisible by 7")
#     break
# else:
#     print(f"The value {n} is not divisible by 7")
#     print("Try again")

# m = int(input("Please select a number = "))
# if not m % 7 == 0:
#     print(f"The value {m} is not divisible by 7")
# else:
#     print(f"The value {m} is divisible by 7")


# write a program that will display the text "The value of the variable is odd" on the screen if the value of the
# varibale is odd, and otherwise display the text "The specified value is even"

# number_even = int(input("The specified value is = "))
# while not number_even % 2 == 0:
#     print(f"The variable {number_even} is odd")
#     break
# else:
#     print(f"The specified value {number_even} is even")

# if number_even % 2 == 1:
#     print(f"The variable {number_even} is odd")
# else:
#     print(f"The variable {number_even} is even")

# write a program that will display on the screen whether the variable value is divisible by 7, by 5 or by 33.
# if the variable value is not divisible by any of these numbers, the program should display an appropiate messag

# var = int(input("The variable selected is ="))
# if var % 7 == 0 and var % 5 == 0 and var % 3 == 0:
#     print(f"The variable {var} is divisible by 7, by 5 and by 3")
# elif var % 7 == 0 and var % 5 == 0:
#     print(f"The variable {var} is divisible by 7 and by 5")
# elif var % 7 == 0 and var % 3 == 0:
#     print(f"The variable {var} is divisible by 7 and 3")
# elif var % 5 == 0 and var % 3 == 0:
#     print(f"The variable {var} is divisible by 5 and 3")
# elif var % 7 == 0:
#     print(f"The variable {var} is divisible by 7")
# elif var % 5 == 0:
#     print(f"The variable {var} is divisible by 5")
# elif var % 3 == 0:
#     print(f"The variable {var} is divisible by 3")
# else:
#     print(f"The variable {var} is not divisible by 7, 5 or 3")

#write a program that desplays all natural numbers between 0 and 50
# n = 0
# while n < 51 :
#     print(n, end=" ")
#     n += 1

# for n in range(0,51):
#     print(n, end=" ")

#write a program that displays all even numbers between 0 and 100

# n = 0
# while n < 101:
#     print(n, end=" ")
#     n += 1
#
# for m in range(0,101):
#     print(m, end=" ")
#     m += 1

# functiile ne ajuta pentru organizare, pentru a face codul mai clar, au argumente de input si ne calculeaza si genereaza rezultate pe baza lor
"""
Sintaxa unei functii
def function_name(arg1, arg2, arg3)
    instruction 1
    instruction 2
    instruction 3
    instruction n
    return something
"""
# def alba():
#     print("Hakuna matata")
# alba()
# alba()

#daca nu e trecut sa returneze ceva, returnezaza none by default

# def print_name(name, prenume = "Alex"):
#     print(f"Hello, {name} {prenume}!")
# print_name("Ion", "Albert")
# print_name("Vasile")
# print(print_name("Vasile"))

