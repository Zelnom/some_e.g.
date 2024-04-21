print("Welcome to the tip calculator!")
bill = float(input("Please enter the amount of the bill : $"))
number_of_people = int(input("Please enter the number of people that will contribute to cover the bill: "))
if number_of_people in range(0, number_of_people + 1):
    print("Tip percentage options: 12%, 15%, 20%")
    tip_percent = int(input("Please enter the percentage of tip that you would like to give: %"))
    if tip_percent == 12:
        tip_percent = tip_percent / 100
        tip_value = (bill/number_of_people) * tip_percent
        print(f"Your tip is ${tip_value:.1f}")
    elif tip_percent == 15:
        tip_percent = tip_percent / 100
        tip_value = (bill/number_of_people) * tip_percent
        print(f"Your tip is {tip_value:.1f}")
    elif tip_percent == 20:
        tip_percent = tip_percent / 100
        tip_value = (bill/number_of_people) * tip_percent
        print(f"Your tip is {tip_value:.1f}")
    else:
        print("Please choose one of the % specified!")
else:
    print("Insert a valid number of people!")

