# loops with while
# 1. Write a program that displays all natural numbers between 0 and 50.

# n = 1
# while n < 50:
#     print(n)
#     n += 1
#     if n == 49:
#         break
# print(n)

# 2.Write a program that displays all even numbers between 0 and 100.
# a number is even when % 2 equal to 0

# n = 1
# while n < 99:
#     n += 1
#     if n % 2 == 0:
#         print(n, end=" ")
#     if n % 2 == 1:
#         continue

# 3.Write   a   program   that   displays   the   squares   of   all   integers between 0 and 10

# n = 0
# while n < 9:
#     n += 1
#     # print(int(f"{n ** 2}"))
#     sq = n ** 2
#     print(int(sq))

# 4.Using the loop, write numbers from -20 to 20. Then write:
# for n in range(-20, 21):
#     if n % 2 == 0:
#         print(n, end=" ")
#         n += 1

# for n in range(-20,21):
#     if n == 5:
#         continue
#     print(n, end=" ")

# for n in range(-20, 21):
#     if n  > 7:
#         continue
#     print(n, end=" ")

# for n in range(-20, 21):
#     if n % 5 == 0:
#         print(n, end=" ")

# sum = 0
# for n in range(-20, 21):
#     sum = sum + n
# print(sum)

# sum = 0
# for n in range(-20, 21):
#     if n >= 4:
#         sum += 1
# print(sum)

# for n in range(-20, 21):
#     print(f"The number is {n} and his power is {n**2}")
n = 0
for n in range(-20, 21):
    n += 1
    print(f"{n % 10}")
# 5.Write a program that displays numbers that are multiples of 5 and are divisible by 7 within the range from 1500 to 2700

# for n in range(1500, 2500):
#     if n % 5 == 0 and n % 7 == 0:
#         print(n)
#     else:
#     print("Programul s-a termiant")

# n_min = 1500
# n_max = 2700
# while n_min <= n_max:
#     if n_min % 5 == 0 and n_min % 7 == 0:
#         print(n_min)
#     n_min += 1
# print("Programul s-a terminat")




# 6.Write a program that writes numbers from 0 to 6 and omits 3 and 6. Do it in two versions: with and without the continue statement.
# list = []
# a = 0
# while a < 6:
#     if a != 3 and a != 6:
#         list.append(a)
#     a += 1
# print(list)


# for loop
# 1. A 10-element array is given: a_list = [1, 3, 5, 2, 5, 6, 7, 4, 9, 7].
# Write a program that prints: ◦ all digits, ◦ the first 6 digits, ◦ ostatnich cyfr,
# ◦ all even digits, ◦ all digits on odd indexes, ◦ all digits except digit 5,
# ◦ all digits up to and including digit 7, ◦ all digits divisible by 3, ◦ the sum of all digits,
# ◦ the sum of digits greater than or equal to 4, ◦ the smallest and the  largest digit.

# index = 0
# list = [1, 3, 5, 2, 5, 6, 7, 4, 9, 7]
# print(list)
# print(list[:6])
# print(list[4:])
# for ind in list:
#     if ind % 2 == 0:
#         print(f"{ind} even")
#     elif ind % 2 == 1:
#         print(f"{ind} not even = odd")



# 2. Write a program that for the given number of words, e.g. a_list = ['cat',
# 'primer', 'window', 'computer'] will display subsequent items of the list
# together with information about the length of these items.

# a_list = ['cat', 'primer', 'window', 'computer']



# 3. Write a program that for the given list of words, e.g.
# list_of_words = ["spam", "table", "spam", "brown", "air", "malware", "spam", "end"]
# will display only the list items that have no "spam" value. In
# addition, if the list item value is "malware", the program should terminate
# operation immediately. Use the break statement. Search in the Internet
# for information on how the break statement works

# 4. Write a program that will display, one by one, all items together with
# their types for a given list. For the following list:a_list = [4, True, None]
# the program should display the following result:4 <class 'int'>
# True <class 'bool'>
# None <class 'NoneType'>