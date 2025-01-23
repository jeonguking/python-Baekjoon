import sys
data = []
for _ in range(9):
    data.append(list(map(int,sys.stdin.readline().split())))
m = 0

for item in data:
    if m <max(item) :
        m = max(item)
row = 0
col = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == m :
            row = i+1
            col = j+1
            break
print(m)
print(f"{row} {col}")


