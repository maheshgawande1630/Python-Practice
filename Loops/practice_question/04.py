#search for a number x in this tuple using loop

num=(1,4,6,16,25,36,49,64,81,100)
i=0
x=64
while i<len(num):
    if(x==num[i]):
        print("Found at idx",i)
    
    i+=1