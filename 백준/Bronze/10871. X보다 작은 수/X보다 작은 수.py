import sys

a,x = map(int,input().split())

data = list(map(int,sys.stdin.readline().split()))

count = 0
new_li = []
for item in data:
    if item < x :
        new_li.append(item)
print(*new_li)