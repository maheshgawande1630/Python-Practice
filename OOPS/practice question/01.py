#create student class that takes name & marks of 3 subjects as argument in constructor.then create a method to print the average

class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def average(self):
        if len(self.marks)==0:
            return 0
        return sum(self.marks)/len(self.marks)
       

s1 = student("Mahesh",[70,80,90])
print("Hi",s1.name,"Your avg score is",s1.average())            