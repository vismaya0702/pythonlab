def fib(n):
    a,b=0,1
    for i in range(n):
        print(a,end='')
        a,b=b,a+b
no=int(input("Enter number of terms :"))
fib(no)
      
