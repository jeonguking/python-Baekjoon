a,b = map(int,input().split())
num =""
temp = 0
while True:
    temp = a % b
    a //= b
    
    if temp >=10 :
        num+= chr(temp+55)
    else :
        num += str(temp)
    if a == 0 :
        break
print(num[::-1])