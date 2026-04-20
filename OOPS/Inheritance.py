#Inheritance

class Car:

    @staticmethod
    def start():
        print("Car Started")
    

    @staticmethod
    def stop():
        print("Car Stopped")    
        

class ToyotaCar(Car):
    def __init__(self,brand):
        self.brand = brand
        

class Fortuner(ToyotaCar):
    def __init__(self,type):
        self.type = type

car1 = Fortuner("Diesel")
print(car1.type)   
car1.start()
car1.stop()


