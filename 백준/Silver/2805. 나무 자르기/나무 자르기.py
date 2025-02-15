import sys

n,m = map(int,sys.stdin.readline().split())



data = list(map(int,sys.stdin.readline().split()))

start,end = 0,max(data)
mid = 0
while start <= end:
    mid = (start + end)//2
    tree = sum(i-mid for i in data if i > mid)
    
    if tree >= m:
        start = mid+1
    else: 
        end = mid-1
    
print(end)
    

