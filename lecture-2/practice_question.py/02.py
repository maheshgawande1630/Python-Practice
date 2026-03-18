#Write a program to check greatest of 3 num

a=int(input("Enter first num :"))
b=int(input("Enter second num:"))
c=int(input("Enter third num:"))

if (a>=b and a>=c):
    print("a is greatest:", a)
elif(b>=c):
    print("b is greatest:", b)
else:
    print("c is greatest:", c)    