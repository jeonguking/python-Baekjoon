
data = []

j = 0
for i in range(10):
    temp = int(input())
    a = temp % 42
    if not a in data :
        data.append(a)
        j+=1
print(len(data))