#  Write a program to enter mark of 3 subjects from user and store them in dictionary.
# start with an empty dictionary & add one by one . use subject as key & marks as value 


marks ={}

x=input("enter mark of che:")
marks.update({"che":x})

x=input("enter mark of phy :")
marks.update({"phy":x})

x=input("enter mark of math:")
marks.update({"math":x})

print(marks)
