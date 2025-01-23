
s = input()

data = [0 for _ in range(26)]

for i in s:
    if 65 <= ord(i) <=90 :
        data[ord(i)-65]+=1
    elif 97 <= ord(i) <= 122:
        data[ord(i)-97]+=1

m = max(data)

if data.count(m) != 1:
    print("?")
else :
    print(chr(data.index(m)+65))