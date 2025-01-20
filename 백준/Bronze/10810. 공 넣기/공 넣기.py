import sys
n,m = map(int,input().split())
data = [0 for _ in range(n+1)]
for i in range(m):
    i,j,k = map(int,sys.stdin.readline().split())
    data[i:j+1] =[k] * (j-i+1) 

print(*data[1:n+1])

