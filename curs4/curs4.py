# def fun(a , b):
#     if a * b <= 1000:
#         return a * b
#     else:
#         return a + b
# print(fun(100, 20))

"""
Exercise 2:
"""

# for i in range(0,10):
#     print(f"Curent number {i+1}, previous number {i}, sum of the num {i + 1 + i}")

# start = 0
# for i in range(start, 11):
#     if i == start:
#         print(f"Curent number {i}, previous number {i}, sum of the {i+1}")
#     else:
#         print(f"Curent number {i}, previous number {i-1}, sum of the num {i + i - 1}")

"""
Exercise 3
"""

# spin = "pynative"
# for index, char in enumerate(spin):
#     if index % 2 == 0:
#         print(char)
#     else:
#         continue

"""
Exercise 4
"""
# def remove_chars(str2, num):
#     if num > len(str2):
#         return("este prea mare")
#     else:
#         return str2[num:]
#
# print(remove_chars("pynatice", 10))


"""
Exercise 5
"""
lista_x = [10, 10, 4, 5, 10]
lista_y = [5, 6, 9, 2, 4]

def check_number(lista):
    if lista[0] == lista[1]:
        return True
    return False
print(check_number(lista_x))
print(check_number(lista_y))