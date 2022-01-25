a=0
b=1

n=int(input("print fibbonacci till Number? :"))

for i in range(n):
    print(a)
    c=a+b
    a=b
    b=c
