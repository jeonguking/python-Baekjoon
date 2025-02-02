import sys
n = int(input())

data = list(map(int,sys.stdin.readline().split()))


num = 0
for i in range(len(data)):

    find = 0
    if data[i] == 1 :
        continue
    for j in range(2,data[i]):
        if data[i] % j == 0 :
            find += 1

    if find == 0 :
        #소수 일때
        num+=1
print(num)
        

