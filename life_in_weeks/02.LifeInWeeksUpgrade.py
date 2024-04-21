class CustomException(Exception):

    print("Welcome")
    print("We will calculate how many weeks you have left until the age of 90 years old")


try:
    age = int(input("Specify your age here: "))

    if 0 < age < 90:
        years = 90 - age
        number_of_weeks = years * 52
        print(f"For your age of {age} years, you have {number_of_weeks} weeks left to live if you are lucky")

    else:
        raise CustomException("Please enter a valid age!")


except ValueError:
    print("ERROR: Please enter a number for age! Try again!")

