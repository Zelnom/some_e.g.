print("Thank you for choosing Pizzeria del Gatito!")
print("For Order information:")
print("S-small, M-medium, L-Large \nY-Yes, N-No")
size = input("What size of pizza would you like? S, M or L? ")


small_pizza = 15
medium_pizza = 20
large_pizza = 25
pep_smal = 2
pep_ml = 3
cheese = 1
if size.upper() !="S" and size.upper() != "M" and size.upper() != "L":
    print("Please select a valid option!")
else:
    add_pepperoni = input("Do you want peperoni? Y or N? ")
    extra_cheese = input("Do you want extra cheese? Y or N? ")
    if size.upper() == "S":
        if add_pepperoni.upper() == "Y" and extra_cheese.upper() == "Y":
            bill = small_pizza + pep_smal + cheese
            print(f"Your total bill will be ${bill}")
        elif add_pepperoni.upper() == "Y" and extra_cheese.upper() == "N":
            bill = small_pizza + pep_smal
            print(f"Your total bill will be ${bill}")
        elif add_pepperoni.upper() == "N" and extra_cheese.upper() == "Y":
            bill = small_pizza + cheese
            print(f"Your total bill will be ${bill}")
        else:
            bill = small_pizza
            print(f"Your total bill will be ${bill}")
    elif size.upper() == "M":
        if add_pepperoni.upper() == "Y" and extra_cheese.upper() == "Y":
            bill = medium_pizza + pep_ml + cheese
            print(f"Your total bill will be ${bill}")
        elif add_pepperoni.upper() == "Y" and extra_cheese.upper() == "N":
            bill = medium_pizza + pep_ml
            print(f"Your total bill will be ${bill}")
        elif add_pepperoni.upper() == "N" and extra_cheese.upper() == "Y":
            bill = medium_pizza + cheese
            print(f"Your total bill will be ${bill}")
        else:
            bill = medium_pizza
            print(f"Your total bill will be ${bill}")
    elif size.upper() == "L":
        if add_pepperoni.upper() == "Y" and extra_cheese.upper() == "Y":
            bill = large_pizza + pep_ml + cheese
            print(f"Your total bill will be ${bill}")
        elif add_pepperoni.upper() == "Y" and extra_cheese.upper() == "N":
            bill = large_pizza + pep_ml
            print(f"Your total bill will be ${bill}")
        elif add_pepperoni.upper() == "N" and extra_cheese.upper() == "Y":
            bill = large_pizza + cheese
            print(f"Your total bill will be ${bill}")
        else:
            bill = large_pizza
            print(f"Your total bill will be ${bill}")