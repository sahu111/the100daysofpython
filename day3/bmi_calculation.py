# input from user height and weight
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

#bmi calculation
bmi = round(weight/height**2)
print(f"Your BMI is {bmi}")
if bmi <= 18.5:
    print(f"Hey! You are underweight.")
elif 18.5 < bmi <= 25:
    print(f"Congrats! You have a normal weight.")
elif 25 < bmi <= 30:
    print(f"Look! You are slightly overweight.")
elif 30 < bmi <= 35:
    print(f"You are obese.")
else:
    print(f"You are clinically obese.")
    