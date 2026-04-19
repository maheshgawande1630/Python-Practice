#WAP to find the factorial of first n numbers 

n=int(input("Enter a num:"))

fact=1
for i in range(1,n+1):
    fact*=i
    i+=1

print(fact)