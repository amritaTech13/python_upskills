
def say_hello():
    print("hello ji")

def funct(fun):
    def nasted_Fun():
        print(f'function {fun.__name__} is about to run')
        fun()
    return nasted_Fun   
# sey_helo = funct(say_hello)
# sey_helo()

# direct also we can apply logger decotator
@funct
def say_hello():
    print("hello ji")
say_hello()    