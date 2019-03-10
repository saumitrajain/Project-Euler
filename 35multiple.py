
def multiple35(n):
    x=0
    for i in range(1,n):
        if i%3==0 or i%5==0:
            x=x+i
            print x
    return x
n = input()
print multiple35(n)       
            