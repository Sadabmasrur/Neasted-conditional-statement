print("Welcome to South Point School and Collage")
print("Please enter your age and weight to take admission.\n")

age = int(input("How old are you?-- "))
weight = int(input("Enter your weight in kg:-- "))

if age >= 12 and weight >= 40:
    if age <= 18 and weight <= 90:
        print("Congratulations!You are allowed for the class!")
    else:
        print("Sorry, you are not eligible for the class due to age or weight restrictions.")
else:
    print("Sorry, you do not meet the minimum age and weight requirements.")
