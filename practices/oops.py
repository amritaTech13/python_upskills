
class Person:
    def __init__(self, name): # __init__ always require if you are sending arg in created obj from this class otherwise python dont know about arg where to use it. It is construtor
                              # __init__ it not mandotry alwys incase if your not sending any arg in obj which created from this class                                  
        self.name = name
    def printName(self):
        print(f"Hi my name is {self.name} and I'm a react developer!")    

obj1 = Person("Amrita")    
obj1.printName()
