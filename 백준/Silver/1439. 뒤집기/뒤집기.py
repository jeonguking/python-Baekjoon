n = input()
s = int(n)

result = 0
num = 0
t = 1
k = 0
min  = 0


for i in range(len(n)):
    if i == 0 :
        k = int(n[0])
    else:
        if int(n[i]) != k:
            result+=1
            k = int(n[i])
        
result += 1

print(result//2)
