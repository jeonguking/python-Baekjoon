import sys

n,m = map(int,sys.stdin.readline().split())

data = list(map(int,sys.stdin.readline().split()))

data.sort()

max = -1

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            sum = data[i]+data[j]+data[k]
            if sum <= m :
                if max < sum:
                    max = sum

print(max)

