import sys

n = int(sys.stdin.readline())

datan = list(map(int,sys.stdin.readline().split()))

m = int(sys.stdin.readline())

datam = list(map(int,sys.stdin.readline().split()))

num = [0 for _ in range(20000001)]

for i in range(len(datan)):
    temp = 0
    if datan[i] < 0 :
        temp = -datan[i]
    elif datan[i] > 0:
        temp = 10000000+datan[i]
    num[temp]+=1

for i in range(len(datam)):
    temp = datam[i]
    if temp < 0 :
        temp = -temp
    elif temp > 0 :
        temp += 10000000
    print(num[temp],end=' ')




