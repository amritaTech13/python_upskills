

class Bank:
    def __init__(self,  bank_account ):
        self.bank_account = bank_account
        self.__balance = 0

    def deposite(self, __balance):
        if __balance < 0:
            print('Please enter valid amount in positive')
        else:    
            self.__balance += __balance 
        print(f"Deposite Amount: {__balance}")
        self.show___balance()

    def withdra(self,withdra):
        if withdra > self.__balance:
            print("Sorry, you dont have suffiecient amount in your account")
        elif withdra < 0:
            print("widthrawal amount should be in positive")    
        else:    
            self.__balance -= withdra
        print(f"Withdra Amount: {withdra}")
        self.show___balance()

    def show___balance(self):
        print(f"__balance: {self.__balance}")    

sbiBank = Bank(123) 
sbiBank.deposite(1000)   
sbiBank.deposite(1200) 
sbiBank.withdra(200)
# sbiBank.__balance :attribute error becuase it is private encabulation hinding property from outside
