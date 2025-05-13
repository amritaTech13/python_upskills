

n = int(input("Enter number: "))

def prime_number(n):  
    if n<=1:
        return print(f" {n} is not prime nuber") 
    
    for i in range(2, n):
        if( n % i == 0 ):
            return print(f" {n} is not prime nuber") 
    else: 
        return print(f" {n} is prime nuber") 

prime_number(n)     
  