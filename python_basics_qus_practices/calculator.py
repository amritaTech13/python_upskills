

a = int(input("Enter first number: "))
b = int(input("Enter second number:"))

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b
def multiplication(a,b):
    return a * b

def divide(a,b):
    return a/b

print(" --Calculator--")
print("1.Addition")
print("2.Subtract")
print("3.Multiplicate")
print("4.Divide")

option = int(input("Enter no. option: "))

if option == 1:
   result =  add(a,b)
   print(f"{result}")
elif option == 2:
   result = subtract(a,b)  
   print(f"{result}")  
elif option == 3:
   result = multiplication(a,b)   
   print(f"{result}")  
elif option == 4:
   result = divide(a,b)  
   print(f"{result}")    





