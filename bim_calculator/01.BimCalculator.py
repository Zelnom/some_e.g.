print("Welcome to BMI Calculator!")
height = float(input("Enter your height in meters (e.g: 1.55): "))


if height > 0:
    weight = int(input("Please insert your weight in kilograms: "))
    bmi = weight / (height ** 2)
    if weight > 0:
        if bmi < 18.5:
            print(f"Your BMI is {bmi:.2f}. You are underweight!")
        elif 18.5 < bmi < 25:
            print(f"Your BMI is {bmi:.2f}. You have normal weight!")
        elif 25 < bmi < 30:
            print(f"Your BMI is {bmi:.2f}. You are slightly overweight!")
        elif 30 < bmi < 35:
            print(f"Your BMI is {bmi:.2f}. You are obese!")
        else:
            print(f"Your BMI is {bmi:.2f}. You are clinically obese!")

    else:
        print("Please insert a valid weight!")
else:
    print("Please insert a valid height!")
