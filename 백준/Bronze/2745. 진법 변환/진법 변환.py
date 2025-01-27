a,b = input().split()

len = len(a)-1
b = int(b)
num = 0
for item in a:
    if item.isalpha() :
        num += (b** len) *(ord(item)-55)
    else :
        num += (b**len) * int(item) 
    len-=1
print(num)


