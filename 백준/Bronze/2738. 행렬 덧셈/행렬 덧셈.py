
n,m = map(int,input().split())

data = []
data2 = []

for i in range(n):
    temp = list(map(int,(input().split())))
    data.append(temp)
for j in range(n):
    temp = list(map(int,(input().split())))
    data2.append(temp)

result = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        result[i][j] = data[i][j]+data2[i][j]

for row in result:
    print(*row)

