def algo(n):
    while(n>0 and n!=1):
        if(n%2==0):
            n=n/2
            print(n)
        else:
            n=(n*3)+1
            print(n)
    return n 
print(algo(10))
