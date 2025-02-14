import sys

n = int(sys.stdin.readline())

data = []

for i in range(n):
    data.append(sys.stdin.readline().rstrip())

ddata = list(set(data))
sorted_data = sorted(ddata,key=lambda x: (len(x),x))


for i in sorted_data:
    print(i)
    