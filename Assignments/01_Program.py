# n = int(input("Enter your age: "))
# print(f"After 5 year your age will be {n+5}")

def printAge():
    while True:
       
        try:
            age = int(input("Enter your Age: "))
            name = input("Enter your name: ")

            if not age :
                print("Please enter your age. It can not be empty")
                continue
            if not name  :
                print("Please enter name. It can not be empty")
                continue
            if age < 0:
                print("age can not be in negative")  
                continue
            break
        except ValueError:
            print("Please enter valid age")    
    print(f"Hi {name}, your age will be {age + 5} after five years!")

printAge()
