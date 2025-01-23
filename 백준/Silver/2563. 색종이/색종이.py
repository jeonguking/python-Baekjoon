
data = [[0 for _ in range(100)] for _ in range(100)]

num = int(input())

for _ in range(num):
    n,m = map(int,input().split())
    for row in range(n,n+10):
        for col in range(m,m+10):
            data[row][col] = 1
result = 0

for row in range(100):
    for col in range(100):
        if data[row][col] == 1:
            result+=1
print(result)
