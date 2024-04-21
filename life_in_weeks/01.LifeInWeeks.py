print("Welcome")
print("We will calculate how many weeks you have left until the age of 90 years old")
age = int(input("Specify your age here: "))


if 0 < age < 90:
    years = 90 - age
    number_of_weeks = years * 52
    print(f"For your age of {age} years, you have {number_of_weeks} left to live if you are lucky")
else:
    print("Please try a valid age")


