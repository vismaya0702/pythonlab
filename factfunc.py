def fact(n):
    f=1
    for i in range(2,n+1):
        f=f*i
    return f
a=int(input("Enter the number :"))
fa=fact(a)
print("Factorial of",a,"is :",fa)
