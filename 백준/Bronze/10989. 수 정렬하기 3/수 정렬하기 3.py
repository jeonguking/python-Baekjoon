import sys

n = int(sys.stdin.readline().rstrip())
data = [0]*10001

for _ in range(n): 
    data[int(sys.stdin.readline().rstrip())-1]+=1

for i in range(10001):
    if data[i] == 0:
        continue
    for j in range(data[i]):
        print(i+1)
