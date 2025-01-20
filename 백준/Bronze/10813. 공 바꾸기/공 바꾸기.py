import sys

n,m = map(int,sys.stdin.readline().split())
data = [i for i in range(1,n+1)]

for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    temp = data[a-1]
    data[a-1] = data[b-1]
    data[b-1] = temp

print(*data[0:n+1])