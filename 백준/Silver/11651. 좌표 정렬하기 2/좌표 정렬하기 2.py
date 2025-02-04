import sys
data = []
n = int(sys.stdin.readline())

for _ in range(n):
    data.append(list(map(int,sys.stdin.readline().split())))
data.sort(key =lambda x: (x[1],x[0]))

print('\n'.join([f'{i} {j}' for i,j in data]))

