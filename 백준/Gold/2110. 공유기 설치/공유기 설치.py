import sys

n,c = map(int,sys.stdin.readline().split())
data = []
for _ in range(n):
    data.append(int(sys.stdin.readline().rstrip()))

data.sort()

start,end = 1, data[-1]-data[0]

result = 0
while start <= end:
    mid = (start+end)//2
    count = 1
    last = data[0]

    for i in range(1,n):
        if data[i]-last >= mid:
            count +=1
            last = data[i]

    
    if count >= c :
        result = mid
        start = mid+1
    else :
        end = mid-1


print(result)


