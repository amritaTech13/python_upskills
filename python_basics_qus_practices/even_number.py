n = [3,2,6,5,48,18,8]

def even_num(n):
    even = []
    i = 0
    for i in n:
        if i % 2 == 0:
            even.append(i)
    return even
val = even_num(n)
print(f"Even numbers: {val}")