import sys
n,k = map(int,sys.stdin.readline().split())

data = []
data.extend(map(int,sys.stdin.readline().split()))

data.sort()

print(data[-k])


