4"""
tkinter -> librarie pentru interfata grafica
"""

"""
Instructiunile de control : IF ELIF ELSE
ne permit sa avem control asupra codului
"""

# vreme = "soare"
# if vreme == "ploaie":
#     print("Call uber!")
# else:
#     print("Mergem pe jos!")

"""
corpul if-ului /elif-ului/ else tine cat e identarea
putem avea oricate instructiuni dorim in interiorul blocurilor IF/ELIF/ELSE
putem avea si blocuri de IF/ELIF/ELSE sau loop-uri in interior
"""

# vreme = "ploaie"
# if vreme == "ploaie":
#     print("Call uber!")
# else:
#     print("Mergem pe jos!")
# print("Din pacate tot trebuie sa ma duc la munca")


# vreme = input("Cum este vremea afara?\n")
# if vreme == "ploaie":
#     print("Call uber!")
# else:
#     print("Mergem pe jos!")
# print("Din pacate tot trebuie sa ma duc la munca")

"""
putem aveam constructia urmatoare:
 - doar if
 - if elif
 - if else
 - if elif else
"""

""" IF """

# vremea = input("Cum este vremea afara?\n")
# if vremea == "ploaie":
#     print("Avem nevoie de umbrela!")

""" IF ELIF    IF-afiseaza toate variantele"""
# var1 = 1
# if var1 == 1:
#     print(f"On first if var ={var1}")
#     var1 = 3
# if var1 == 3:
#     print(f"On second if var ={var1}")
#     var1 = 5
# if var1 == 5:
#     print(f"On third if var ={var1}")
#     var1 = 10
# print(f"At the end var = {var1}")


# var1 = 1
# if var1 == 1:
#     print(f"On first if var ={var1}")
#     var1 = 3
# elif var1 == 3:
#     print(f"On second if var ={var1}")
#     var1 = 5
# elif var1 == 5:
#     print(f"On third if var ={var1}")
#     var1 = 10
# print(f"At the end var = {var1}")

# var1 = 1
#
# if var1 == 3:
#     print("Var is equal 1")
# else:
#     print("Var is not equal 1")

""" IF ELIF ELSE"""

# vreme = "soare"
#
# if vreme == "ploaie":
#     print("Avem nevoie de umbrela")
# elif vreme == "furtuna":
#     print("ori mergem cu uber ori avem nevoie si de umbrele si de pelerina")
# else:
#     print("Putem merge pe jos")

"""
Daca nu exista else si niciuna dintre conditii nu a fost adevarata el nu va intra pe niciun branch si va mege la
urmatoarele instructiuni de mai jos de constructia noastra
Putem avea oricate clauze elif(dar doar dupa ce avem un if deasupra 
"""

# var1 = 1
# if var1 == 0:
#     print("Var = 0")
# elif var1 == 2:
#     print("Var == 2")
# elif var1 == 5:
#     print("var1 == 5")
# elif var1 == 9:
#     print("var1 == 9")
#
# print("Am terminat de executat codul")


"""
if condition1 == True and condition2 == True
    instruction1
    instruction2
    ............
elif condition1 == True and condition == True
    instruction1
    instruction2
    ............
elif condition1 == True and condition == True
    instruction1
    instruction2
    ............
else -> nu are conditie(aici nu mai suntem pretentiosi ci cand totul din ordinea de prioritati (IF ELIF) nu este adevarat
     -> ne multumim cu ce primim
    instruction1
    instruction2
    ............
"""

# var1 = 1
# var2 = 2
#
# if var1 == 1 and var2 == 2:
#     print(f"var1 equal 1 and var2 equal2")
# else:
#     print(f"or var1 not equal 1 or var2 not equal 2")

"""
IF ELSE single line
"""
# var1 = 12
# var2 = 5  if var1 > 10 else 1000
# print(var2)

"""
if elif else single line
"""

var1 = 6
# evalueaza prima data daca var1 e mai mic decat 10, daca e adevarat asigneaza valoarea 5 lui var 2
# daca nu e adevarat intra pe else unde avem 2000 if var1 > 10 else 10
# evalueaza daca var1 este mai mare ca 10 si daca e adevarat asigneaza valoarea 200 lui var2 altfel valoarea 10
var2 = 5 if var1 < 10 else 2000 if var1 > 10 else 10
"""
if var1 < 10:
    var2 = 5
elif var1 > 10:
    var2 = 2000
else:
    var2 = 10

v2
if var1 < 10

"""
