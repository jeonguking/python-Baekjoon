import sys

k,n = map(int,sys.stdin.readline().split())

data =[]
for _ in range(k):
    data.append(int(sys.stdin.readline().rstrip()))


start,end = 1,max(data)

while start <= end:
    mid = (start+end)//2
    count = 0
    for cable in data:
        count+=cable//mid
    if count>=n:
        start = mid+1
    else:
        end = mid-1
print(end)    
