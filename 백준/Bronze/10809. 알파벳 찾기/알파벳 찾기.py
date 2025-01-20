data = [-1 for _ in range(26)]

s = input()
i = 0
for item in s:
    if data[int(ord(item))-97] == -1 :
        data[int(ord(item))-97] =  i
    i+=1

print(*data)