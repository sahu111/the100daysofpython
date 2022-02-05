print("Welcome to the tip calculator!")

#input from user
total_bill = float(input("What was the total bill? $"))

#input from user
tip_percent = int(input("What percentage tip would you like to give?  any%? "))

#input from user
number_of_people = int(input("How many people to split the bill? "))


#tip calculation
tip = total_bill * (tip_percent/100)

#total bill + tip divides in each person
to_pay_each = (total_bill + tip) / number_of_people

#total bill ka round figure 2 decimal places tk
rounded_bill = round(to_pay_each, 2)


print(f"Each person should pay: {rounded_bill}")
print("Updated in splitwie :) !")