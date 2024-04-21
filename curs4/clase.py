# class Dog:
#     def __init__(self, rasa, culoare, varsta, nume):        # grija sa fie __init__ nu __int__
#         self.rasa = rasa
#         self.culoare = culoare
#         self.varsta = varsta
#         self.nume = nume
#
# clifford = Dog("maidanez", "rosu", 12, "Clifford")
# azorel = Dog("beagle", "maro", 3, "Azorel")
# print(clifford)
# print(azorel)


"""
___str__  -> reprezentarea obiectului din clasa respectiva
"""
# class Dog:
#     def __init__(self, rasa, culoare, varsta, nume):        # grija sa fie __init__ nu __int__
#         self.rasa = rasa
#         self.culoare = culoare
#         self.varsta = varsta
#         self.nume = nume
#     def __str__(self):
#         return f"Pe cainele meu il cheama {self.nume}, e din rasa {self.rasa}, e de culoare {self.culoare} si are "\
#                f"{self.varsta} ani."
#
# clifford = Dog("maidanez", "rosu", 12, "Clifford")
# azorel = Dog("beagle", "maro", 3, "Azorel")
#
# # print(clifford)
# # print(azorel)
# #
# # print(clifford.culoare)
# # azorel.varsta += 1
# # print(azorel)
#
# object_string = clifford.__str__()
# print(clifford)

"""
modificari de acces:
-> public self.name
-> protected self._name
-> private self.__name
"""

"""PUBLIC"""
# class Person:
#     def __init__(self, first_name, last_name):
#         self.fname = first_name
#         self.lname = last_name
#
#
# p1 = Person("Ion","Ionescu")
# print(p1.fname)
# print(p1.lname)
# p1.lname = "Georgescu"
# print(p1.fname)
# print(p1.lname)

"""PROTECTED"""
# class Person:
#     def __init__(self, first_name, last_name):
#         self._fname = first_name
#         self._lname = last_name
#
# p1 = Person("Georgescu", "Popescu")
# print(p1._fname)
# print(p1._lname)

"""PRIVATE"""
# class Person:
#     def __init__(self, first_name, last_name):
#         self.__fname = first_name
#         self.__lname = last_name
#
# p1 = Person("Georgescu", "Popescu")
# print(p1.__fname)         # error private aatr
# print(p1.__lname)         # error private aatr
#

# v2.

# class Person:
#     def __init__(self, first_name, last_name):
#         self.__fname = first_name
#         self.__lname = last_name
#     def __str__(self):
#         return f"Last name: {self.__lname}, First name: {self.__fname}"
#
# p1 = Person("Georgescu", "Popescu")
# print(p1)
# # print(p1.__fname)
# # print(p1.__lname)

# class Person:
#     def __init__(self, first_name, last_name):
#         self.__fname = first_name
#         self.__lname = last_name
#
#     def get_first_name(self):
#         return self.__fname
#
#     def set_first_name(self, new_name):
#         self.__fname = new_name
#
#     def __str__(self):
#         return f"Last name: {self.__lname}, First name: {self.__fname}"
#
# p1 = Person("Dorel", "FaraCurent")
# print(p1)
# print(p1.get_first_name())
# p1.set_first_name("Ionel")
# print(p1)
# print(p1.get_first_name())


"""getter and setter"""

# class Person:
#     def __init__(self, first_name, last_name):
#         self.__fname = first_name
#         self.__lname = last_name
#
#     @property
#     def get_first_name(self):
#         return self.__fname
#
#     def set_first_name(self, new_name):
#         self.__fname = new_name
#
#     def __str__(self):
#         return f"Last name: {self.__lname}, First name: {self.__fname}"


"""
modificatorii de acces sunt folositi si la metode
metodele pot fi si ele public, protejate sau private
"""

# def test():
#     a = 5
#     return a**2
# test()
#
# print(a)
# print([1, 2].extend([3, 4]))

s={3, 4, 1, 1}
print(max(s))