
n,m = map(int,input().split())
data = list(i for i in range(1,n+1))

for _ in range(m):
    i,j = map(int,input().split())
    data[i-1:j] = reversed(data[i-1:j])

print(*data)    
