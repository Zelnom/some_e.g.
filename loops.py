"""
for var in iterable:
    instruction1
    instruction2
    ............

range(stop) -> ne va crea un iterabil si va merge de la 0, valoarea default a lui start cu step de 1
pana la stop exlusiv(stop-1)
range(start, stop) -> ne va crea un iterabil si va merge de la start(inclusiv) pana la stop exclusiv(stop-1) cu step1
range(start, stop, step) -> ne va crea un iterabil si va merge de la start(inclusiv) pana la stop(exclusiv) cu stepul
de
"""

#iteratie - de cate ori va intra

# for i in range(5):
#     print(i)
#     print(i**2)
# daca a executat prima instructiune si cea de a doua =>> a realizat blocul... iteratii => de cate ori a realizat blocul

# my_list = [1, 7, 21, 5, 3, 10]
# for number in my_list:
#     print(f"Inside for: {number}")
# print(f"Outside for: {number}")
# putem risca daca avem lista goala

# my_dictionary = {
#     "key1": 1,
#     "key2": 2,
#     "key3": 34
# }
#
# for key in my_dictionary:
#     print(f"key {key} and value: {my_dictionary.get(key)}")


# for number in range(10):
#     if number == 3 or number == 6:
#         print("continue", end=" ")
#         continue
#     print(number, end=" ")
# else:
#     print()
#     print(f"Outside for number is equal {number}")

"""
INSTRUCTIUNEA BREAK
-> cand intalneste instruciunea break ne iese din loop
"""

# list1 = [1, 8, 21, 1213, 99, 666, 15, 81]
# for number in list1:
#     if number == 99:
#         print("BREAK")
#         break
#     print(f"Number is equal {number} ")
# else:
#     print(f"Value of number after the end of the for loop {number}")

# dupa ce am gasit nu mai verificam si pe restul


"""
enumerate
ne returneaza un tuplu cu
"""

# list_of_words = ["mere", "pere", "portocale", "kiwi", "pepene"]
# for index, word in enumerate(list_of_words):
#     print(f"{index} {word}")

# list_of_words = ["mere", "pere", "portocale", "kiwi", "pepene"]
# for word in enumerate(list_of_words):
#     print(f"{word[0]}")            # sau [1]

"""
while:
while condition
    instruction1
    instruction2
    instruction to help us to end the while loop
"""
# number = 5
#
# while number >= -0:
#     print(number)
#     number -= 1

# list1 = [7, 9, 21, 18, 3, 5]
# index = 0
# while index < len(list1):
#     print(list1[index])
#     index += 1
"""
FOR il folosim pentru un numar finit de iteratii
WHILE de cele mai multe ori il folosim pentru un numar variabil de iteratii...nu stim cate iteratii avem nevoie
"""

# number1 = 120000000
# number2 = 200000000000000000000
# divisor = number1 if number1 < number2 else number2
# while True:
#     if number1 % divisor == 0 and number2 % divisor == 0:
#         print(divisor)
#         break
#     divisor -= 1
#     if divisor <= 2:
#         print(1)
#         break


"""
poate sa existe loop in interiorul altui loop
"""

# for num1 in range(5):
#     for num2 in range(5):
#         print(f"{num1} {num2}")

# index1 = 0
# index2 = 0
# while index1 < 5:                                                   # 0 < 5
#     while index2 < 5:                                               # 0 < 5  1 < 5      2 < 5
#         print(f"{index1} {index2}")                                 # 0      0   1      0 2
#         index2 += 1                                                # i2 = 1   i2 = 2    i2 = 3
#     index1 += 1                                         #............................. i1 = 1
#     index2 = 0  # de fiecare data cand il crestem trebuie sa il resetam     #_____________________ i2 = 0
# # la for nu trebuie sa resetam valoarea, pe cand la while este necesar altfel nu se mai revine

# while index1 < 5 and index2 < 5:             #NU E RECOMANDATA!! CONTRAINTUITIV
#     print(f"{index1} {index2}")
#     index2 += 1
#     if index2 == 4
#         index1 += 1
#         index = 0

""" while are si el continue si break """

number = 0
while number < 5:
    print(number)
    if number == 2:
        number += 1
        continue
    number += 1


fibonacci_list = [0, 1]
n = 0
while n < 50: