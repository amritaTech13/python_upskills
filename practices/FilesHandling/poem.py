# search 'twinkle' in given text is there or not
keyWord ='twinkle'
find= False
with open('./FilesHandling/poem.txt','r') as readl:
    content = readl.read()
    print(content)
    if keyWord in content:
        find =  True

print(find)