import sys

m = int(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline().rstrip())

sum = 0
first = 0
temp = 0 
for i in range(m,n+1):
    if i == 1 :
        continue
    if i == 2 :
        first = 2
        temp+=1
    find = 0
    for j in range(2,i):
        if i % j == 0 :
            find +=1
    if find == 0 :
        if temp == 0 :
                first = i
                temp+=1
        sum+=i

if sum == 0 :
    print("-1")
else : 
    print(sum)
    print(first)