import sys
n = int(input())

data = list(map(int,sys.stdin.readline().split()))

data.sort()


if n == 1 :
    print(data[0])
else :
    print(data[(n-1)//2])


