# leap year program 
year = int(input("Which year do you want to check for leap year? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is Leap year.")
        else:
            print(f"{year} is Not leap year.")
    else:
        print(f"{year} is Leap year.")
else:
    print(f"{year} is Not leap year.")