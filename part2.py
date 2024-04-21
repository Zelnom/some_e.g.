""" Dictionary
dictionarele sunt o colectie de date de tip key:value
ele se definesc prin acolade
cheile trebuie sa fie de tip imutabil si sa fie unice
"""

my_dictionary1 = {}
my_dictionary2 = dict()
print(my_dictionary1)
print(my_dictionary2)
print(type(my_dictionary1))
print(type(my_dictionary2))

agenda_telefon = {"Ionel": "0722334455",
                  "Gigel": "0799887766",
                  "Vasile": 712345675}
print(agenda_telefon)

print(agenda_telefon["Ionel"])
print(agenda_telefon.get("Ionel"))    # Recomandat
""" diferenta intre dictionary[key] si disctionari.get[key]
dictionary[key] -> daca nu avem cheia respectiva ne da eroare
dictionary.get(key, value) -> daca nu avem cheia respectiva, ne returneaza None by default, sau valoarea specificata 
"""
# print(agenda_telefon["Popesc"])
print(agenda_telefon.get("Popescu"))
print(agenda_telefon.get("Popescu", "Nu am cheia respectiva"))

my_dictionary = {
    "key1": 1,
    "key2": 2,
    "key1": 5
}
print(my_dictionary)

""" cum adaugi o noua cheie in dictionar """
my_dictionary[9] = 3
print(my_dictionary)
my_dictionary["key2"] = 99   #doar cu paranteze [] cand modificam cheia
print(my_dictionary)
# nu se poate indexa dictionarul !!
# EROARE, nu putem avea cheie de tip mutabil in dictionar

# my_dictionary_mutable_key = {
#     "key1": 1,
#     [1, 5, 6, 8]: 3
# }
# print(my_dictionary_mutable_key)

""" mutabil vs imutabil
mutabil sunt tipurile de date carora le putem modifica valoarea dupa bunul plac si ID-ul/adresa din memorie ramane la fel
imutabil -> nu putem modifica valoarea lor sau daca modificam adresa lor din memorie se schimba
"""
var1 = 5
print(var1)
print(id(var1))
var1 = 7
print(var1)
print(id(var1))

list1 = [7, 12, 32, 2, 8, 1]
print(list1)
print(id(list1))
list1[2] = 999
print(list1)
print(id(list1))

# lista -> mutabil, variabile -> imutabile

# dict1= {
#     "x": 123,
#     "y": 763,
#     "z": "fsda"
# }
# print(id(dict1))
# dict1["x"] = "ABC"
#
# print(dict1)
# print(id(dict1))
#
# dict2 = {
#     "1": 1,
#     "dict1": dict1
# }
# print(dict2)
# print(id(dict2))

dictionary1 = {
    "key1": 1,
    "key2": 2,
    "key3": 3,
    4: 199
}
print(dictionary1)
dictionary1.pop("key2")
print(dictionary1)
del dictionary1["key3"]
print(dictionary1)
# del dictionary1["key3"]   # da eroare daca nu exista cheia
# print(dictionary1)

""" tuple
asemanator listei, se bazeaza pe index doar ca este imutabil
odata ce e creat nu putem modifica valorile din interiorul lui, maxim putem sa ii asignam un alt tuplu
specific pentru el sunt ()
PENTRU A CREA UN TUPLU CU UN SINGUR ELEMENT FOLOSIM URMATOAREA SINTAXA my_tuple = (1,)
"""

tuple1 = ()
tuple2 = tuple()
print(tuple1)
print(tuple2)
print(type(tuple1))
print(type(tuple2))

tuple3 = (1)
print(tuple3)
print(type(tuple3))

tuple4= (5,)
print(tuple4)
print(type(tuple4))
#intrebare la interviuri : cum declari in tuple un element dintr-un singur caracter

tuple23 = (5, 85, 64, 84)
print(tuple23[2])
print(tuple23[-2])
print(tuple23[1:])
print(tuple23[::-1])
list1 = [2, 9, 8]
tuple1 = (1, 3, 5, list1, "abc")
print(tuple1)
print(id(tuple1))
list1[1] = 1000
print(tuple1)
print(id(tuple1))

tuple1= (1, 3, 5, [900, 31, 402], "abc")
print(tuple1)
print(id(tuple1))
tuple1[3][1] = 4777
print(tuple1)
print(id(tuple1))

# tuplex = (1, 3, input("introdu un nr: "), 100)
# print(tuplex)

""" SET/fratele "handicapat" 
este o colectie de date, care are valori unice, este mutabil, dar neordonat
specifice sunt acoladele {}
"""
my_set = set()
print(my_set)
print(type(my_set))

my_set = {1, 18, 2, 9, 99}
print(my_set)
print(type(my_set))

my_str_set = {"caine", "pisica", "elefant", "rinocer", "pisica"}        # valorile nu se repeta
print(my_str_set)
print(type(my_str_set))

nume= input("Introduceti numele: ")
prenume= input("Introduceti prenumele: ")
print(f"{prenume} {nume}")

#sau
print("{1} {0}". format(nume, prenume))


