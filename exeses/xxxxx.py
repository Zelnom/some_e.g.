# # my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # print(my_list[0])
# # print(my_list[8])
# # ​
# ### key error ###
# # ​
# class ExceptieSmechera(Exception):
# 	pass
# try:
#     students = {'solo': 9, 'bobonete': 10, 'bordea': 7}
#     print(students['solo'])
#     print(students['bogdan'])

# x = lambda a : a + 10
# print(x(5))
#
# square_lambda = lambda x: x*x
# equals_lambda = lambda x,y: x==y
# print(square_lambda(4))
# print(equals_lambda("abc", "bca"))
# print(equals_lambda("abc", "abc"))
# print("\n\n")

items = [1, 2, 3, 4, 5]

squared_temp = map(lambda x: x*x, items)
squared = list(map(lambda x: x*x, items))
odds_temp = filter(lambda x: x%2 == 1, items)
odds = list(filter(lambda x: x%2, items))

print(f"items:{items}")
print(f"squared_temp:{squared_temp}")
print(f"squared:{squared}")
print(f"odds_temp:{odds_temp}")
print(f"odds:{odds}")