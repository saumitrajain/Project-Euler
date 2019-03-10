
def fib(i):
    sum = 0
    for n in range(1,i):
        if n<=1:
            sum=1
        if n%2==0:
            
            if n<=1:
                return 1
            if n==2:
                return 2
            if n>2:
               sum= fib(n-1)+fib(n-2)  
               
               
    print sum         
    
n = input()
print fib(n)       
            