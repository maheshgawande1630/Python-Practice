#Search for a number x in this tuple
#(1,4,9,25,36,49,64,81,100)


squares=(1,4,9,25,36,49,64,81,100,25)

x=25
idx=0

for value in squares:
    if (value==x):
        print("number found at idx",idx)

    idx += 1 
