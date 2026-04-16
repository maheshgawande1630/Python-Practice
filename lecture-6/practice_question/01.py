#WAF to find factorial of n (n is the parameter)


#using while

def fact_while(n):
    fact=1
    while n>0:
        fact*=n
        n-=1
    
    return fact


result=fact_while(6)
print(result)


#using for

def fact_for(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact

result=fact_for(4)
print(result)
