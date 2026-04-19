#creating class
class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks 

#creating object
s1 = student("mahesh",94)
print(s1.name,s1.marks)        