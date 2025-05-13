
# file = open('myfile.txt', 'w')
# file.write('Hi, Amrita\n')
# file.write('How you are?')
# file.close()

# try:
#     file = open('myfile2.txt', 'r')
#     content = file.read()
#     print(content)
#     file.close()
# except FileNotFoundError:
#     print("File not found. Please check the file name")    


# better use with -becuase using 'with' no need to close file everytime python will do automatically

with open('myfile2.txt', 'w') as file:
    file.write("Hi Pratima\n")
    file.write("you are great")

try:
    with open('myfile2', 'r') as file:
        content = file.read()
        print(content)    
   
except FileNotFoundError:
    print("Np file found, please check the file name")    

