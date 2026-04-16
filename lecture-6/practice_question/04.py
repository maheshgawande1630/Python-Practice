#Write a function to check if a number is positive, negative, or zeroWrite a function to check if a number is positive, negative, or zero

def num_type(n):
    if n<0:
        print("Negative")
    elif n>0:
        print("Positive")
    else:
        print("Zero")

num_type(6)
num_type(0)
num_type(-7)            