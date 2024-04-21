my_str = "Si azi murim de cald!"

"""
index in Python incepe de la 0 (in C si java tot de la 0 incep)
indexul 0 insemnand primul caracter din string-ul nostru

"""

"""" Accesarea unui element din string pe baza indexului"""
print(my_str[0])
print(my_str[7])

""" Functia len(str) -> returneaza numarul de caractere(numaratoarea incepe de la 1) """
print(len(my_str))

""" Slice-ing
str[start:stop:step]
start -> de unde incepe substringul nostru(inclusiv indexul de start)       by defaiult startul are valoarea zero
stop -> de unde se termina -1(adica merge pana la stop exclusiv)         by default are valoarea (len(str) -merge pana la ultimul element inclusiv (daca nu e nimic trecut)
step -> pasul cu care va creste indexul nostru               by default are valoarea 1
indexul poate sa fie si negativ(iar atunci incepe de la -1, -1 reprezentand ultimul element din string)
pornind de la start crestem indexul cu step cat timp e mai mic decat stop
"""
print(my_str[7:12])
print(my_str[0:20])
# nu printeaza ultimul caracter intrucat e stopul...daca vrem sa printeze => 21
# daca vrem sa dam print separat => eroare
# print(my_str[21])
print(my_str[0:21:3])
print(my_str[-1])
print(my_str[0:-1])
print(my_str[20:0:-1])
print(my_str[::-1])  # merge dintr-ul capatat in altul
print(my_str[::1])
print(my_str[-5:], my_str[-6::-1], sep="")
print(my_str[-5:] + my_str[-6::-1])
# print(my_str[-6::-1])

""" str.index("char") -> returneaza primul index la care gaseste un caracter sau un alt set de caractere"""
my_str2 = "What a wonderful day!"
print(my_str2.index("w"))
print(my_str2.index("a"))
# print(my_str2.index("z"))            # eroare cand nu gaseste
print(my_str2.index("wonderful"))

""" str.count("char) -> returneaza de cate ori gaseste un caracter/cuvant/substring"""
# print(my_str2.count("a"))
# print(my_str2.count("t"))
# print(my_str2.index("a"))
# print(my_str2.index("a", 3))
# print(my_str2.index("a", 6))
""" functiile str.upper() str.lower() ->returneaza o copie temporara a stringului nostru cu lietere mari sau mici
in functie de caz(upper -> majuscule, lower -> minuscule)
e un fel de deep copy intrucat string-ul original nu este modificat 
"""
print(f" original string: {my_str2}")
print(f" upper string {my_str2.upper()}")
print(f" original string: {my_str2}")
print(f" lower string {my_str2.lower()}")
print(f" original string: {my_str2}")

""" exemplu de functii ale stringurilor 
str.replace(old, new, count)
old -> ce vrem sa inlocuim
new -> cu ce vrem sa inlocuim
count -> de cate ori vrem sa inlocuiasaca, primele n aparitii. by default are valoarea str.count(char), adica inlocuieste 
"""
my_str2 = " What a wonderful day! "
print(my_str2.strip())   # elimina spatiile de la inceput si de la final
print(my_str2)

print(my_str2.replace("a", "z"))        # returneaza o copie a stringului inlocuind old cu new
print(my_str2.replace("a", "z",1))
print(my_str2.replace("a", "z",2))

my_str3 = "Hello from the other side"
print(my_str3.isdigit())

my_str4 = "12345"
print(my_str4.isdigit())
my_str5 = "12345c"
print(my_str5.isdigit())

print(my_str5.split("2"))  #"separatorul este eliminat"
my_str6 = "2123542653c2"
print(my_str6.split("2"))

"""colectii de date/collections- containere sau variabile de tip complex care pot contine mai multe valori
list
"""
# doua abordari
my_list1 = []
my_list2 = list()

print(my_list1)
print(type(my_list1))
print(my_list2)
print(type(my_list2))

my_list3 = [1, 2, 3, "a", "b"]
print(my_list3)
print(type(my_list3))

"""
lista e o colectie neordonata de date mutabile
mutabil vs imutabil
mutabil -> poti modifica valorile
imutabil -> nu poti modifica valorile
"""
my_list = [1, 2, 5, 18, 3, 21, 7]
print(my_list)
print(id(my_list))
my_list[2] = 4
print(id(my_list))
my_list[2] = my_list[5]
print(my_list)
"""listele pot avea alte liste in interior"""

my_list =[5, 2, 4.3, 7j, "abc", [99, 13, 21, 10], True]
print(my_list)
my_list[5][3] = 4
my_list[-2][-3] = 9              # -1 la inceput => True
print(my_list)

my_list =[5, 2, 4.3, 7j, "abc", [99, 13, 21, 10], True]
print(my_list)
print(len(my_list))
my_list.append(False)
print(my_list)
print(len(my_list))
print(len(my_list[-3]))
# append -> adauga la sfarsit un element

""" list.extend(iterabil_lista_tupul_ect) -> extinde lista cu elemente din cea de-a doua lista """
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list1)
print(id(list1))
print(list2)
print(id(list2))

list1.extend(list2)
print(list1)
print(id(list1))
print(list2)
print(id(list2))

""" list.pop(index) -> eliminam un element dintr-o lista 
daca index nu este specificat => eliminam ultimul element
functia pop returneaza si valoarea elementului eliminat
"""
list1.pop()
print(list1)
print(list1.pop())
print(list1)

""" utilitatea returnului functiei pop, poate fi vazuta si la mecanismul de undo redo
la undo avem o lista cu ultimele n comenzi executate
cand dam undo ne elimina ultima comanda din lista si ne adauga comanda in lista de redo
"""
undo = []
redo = []

undo.append("click Home")
print(f"undo list=, {undo}\nredo list:{redo}")
undo.append("search hakuna matata")
print(f"undo list=, {undo}\nredo list:{redo}")
undo.append("click site")
print(f"undo list=, {undo}\nredo list:{redo}")
undo.append("sign in")
print(f"undo list=, {undo}\nredo list:{redo}")
redo.append(undo.pop())
print(f"undo list=, {undo}\nredo list:{redo}")
redo.append(undo.pop())
print(f"undo list=, {undo}\nredo list:{redo}")
undo.append(redo.pop())
print(f"undo list=, {undo}\nredo list:{redo}")

""" sorted(iterabil, reverse) -> returneaza o copie a iterabilului sortat in ordine crescatoare by default
reserse=False by default
sorted nu afecteaza lista initiala 
"""

list8 = [1, 5, 2, 4, 3, 7, 8]
print(sorted(list8))
print(list8)
print(sorted(list8, reverse=True))
print(list8)
print(id(sorted(list8, reverse=True)))
print(id(list8))

""" list.sort(reverse) ->sorteaza lista initiala in ordine crescatoare by default si returneaza None
are impact asupra listei initiale
reverse=False by default
"""
print(list8)
list8.sort()
print(list8.sort())
print(list8)
print(id(list8))
list1.sort(reverse=True)
print(list8)
print(id(list8))

list9 = ["ana", "mere", "are", "pere", "pare", "Zar"]
# le ia alfabetic dupa ASCII
# upper case primul intrucat valoarea lor in ASCII e mai mica
print(list9)
list9.sort()
print(list9)
"""
.count(value) -> numara de cate ori gaseste valoarea in lista
"""
list5 = [7, 2, 1, 1, 3, 5, 7, 8, 7]
print(list5.count(7))
"""
.index(value) -> returneaza primul index la care gaseste valoarea, eroare daca nu exista valoarea in lista
"""
print(list5.index(3))

"""
insert(index, value)
"""
list4 = [5, 8, 2, 9, 12, 7]
list4.insert(3, 7)
print(list4)
"""
.remove(value)
"""
list4 = [5, 7, 2, 9, 12, 7]
print(list4)
list4.remove(7)
print(list4)

# list4 = [5, 7, 2, 9, 12, 7]
# print(list4)
# list4.remove(5)
# print(list4)
# list.pop()
# list.pop()
# list.pop()
# list.pop()
# list.pop()
# print(list4)
# list.pop()
# list.pop()
# print(list4)
""" .clear() """
list4 = [5, 7, 2, 9, 12, 7]
print(list4)
list4.clear()
print(list4)

""" .reverse() """
list4 = [5, 7, 2, 9, 12, 7]
print(list4)
list4.reverse()
print(list4)


lista = [1, 2, 3, 4, 5]
lista2 = lista
lista.clear()
print(lista2)

""" caractere speciale:
\n -> new line
\t -> tab   = 4 spatii
\b -> backspace
\" -> ghilimele
\' -> apostrof
\\ -> backslash 
"""
