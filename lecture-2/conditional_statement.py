"""  Q. Grade studens based on marks

    marks>=90,grade="A"
    90>marks>=80,grade="B"
    80>marks>=70,grade="c"
    70>marks,grade="D"      """


marks=float(input("Enter marks: "))

if(marks<=100 and marks>=90):
        print("Grade=A")
elif(marks<90 and marks>=80):
        print("Grade=B")
elif(marks<80 and marks>=70):
        print("Grade=C")
elif(marks<70):
        print("Grade=D")    
else:
    print("Invalid input")        
                    
