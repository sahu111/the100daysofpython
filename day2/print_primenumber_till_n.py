# low aur hihg be bich range me prime num print krna hai 
low = int(input("low: "))
high = int(input("high: "))

for n in range(low,high+1):
    count = 0
    div = 2
    while div*div<=n:
        if(n % div==0):
            count+=1
            break
        div+=1

    if count==0:
        print(n)
