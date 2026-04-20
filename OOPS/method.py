#methods are functions that belong to object:

#creating class
class student:

    def __init__(self,name):
        self.name = name

    def hello(self):
        print("hello",self.name)

#creating object               
s1 = student("Mahesh") 

#function
s1.hello()
     