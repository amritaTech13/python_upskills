
list = [1,4,2,3,7,6,8,9,10]
def count_num(list):
    count = 0
    i=1
    for i in list:
        if i % 2 == 0:
            count += 1
            
    return count

even = count_num(list)
odd = len(list) - even
print(f"Even number present in your list is {even} and odd is {odd}")