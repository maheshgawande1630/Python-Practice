"""  Q. Grade studens based on marks

    marks>=90,grade="A"
    90>marks>=80,grade="B"
    80>marks>=70,grade="c"
    70>marks,grade="D"      """


marks=float(input("Enter marks: "))

if(100>=marks>=90):
        print("Grade=A")
elif(90>marks>=80):
        print("Grade=B")
elif(80>marks>70):
        print("Grade=C")
elif(70>marks):
        print("Grade=D")    
else:
    print("Invalid input")        
                    
