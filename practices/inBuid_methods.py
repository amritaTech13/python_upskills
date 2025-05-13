import sys 
import logging

count = 10
list = [3,4,1,2]
print( f"list :  {sys.getsizeof(list)}")
list.append(8)
tuples = (5,7,2,9)
dic = {
    'name':"Amrita",
    'lname': 'Rajbhar'
    }
# sys.getsizeof - it return obj's size of given val in byte its including extra memory used by garbase colloter of python merorysize + byte + 
print(f"count : {sys.getsizeof(count)}")
print( f"list :  {sys.getsizeof(list)}")
print(f"tuples: {sys.getsizeof(tuple)}")
print(f"dic: {sys.getsizeof(dic)}")

print(f"count__sizeof : {count.__sizeof__()}")
print( f"list__sizeof :  {list.__sizeof__()}")
print(f"tuples__sizeof: {tuples.__sizeof__()}")
print(f"dic__sizeof: {dic.__sizeof__()}")
# sys.getsizeof(): Use this when we need to assess the total memory usage of an object in a live program. It’s great for tasks like profiling a script handling large datasets or debugging why your application is consuming more RAM than expected. For instance, it helps you see the full impact of a list, including garbage collector overhead, which is key for real-world optimization.
# __sizeof__(): Turn to this when you want to measure an object’s core size without extra overhead, perfect for performance comparisons or algorithm tuning. It’s handy for analyzing whether a list or tuple is more memory-efficient for a specific task, like storing data in a performance-sensitive project, giving you a clear view of the object’s baseline footprint.


l = [1,2,3]
# print(dir(l)) # provide all attribute and methods for that object
# print(help(l)) # provide details information about object or fun
# both use for debugging purpose

class Person:
    ''' i am testing it these info will shown while call help method for this object'''
    def test1(self):
        pass
# print(help(Person))


logger = logging.getLogger()

logger.warning('This is warning you message')
print(logger.info("this is information for you"))
# logger.basicConfig(level = logger.INFO)

x = [1, 2, 3]
y = [1, 2, 3]
z = x
# == --> return True if two obj's values are same 
# is --> return true of two obj pointing to same memory location otherwise false
if x is y:
    print("True")
else:
    print("False")    
if x is z:
    print("True")
else: 
    print("False")   

a = 10
b = a
a = 20
print(id(a))
print(id(b) )   
print(id(a)) 
print(a)
print(b)

