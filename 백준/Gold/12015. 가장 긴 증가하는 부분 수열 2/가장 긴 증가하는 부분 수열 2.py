import sys

from bisect import bisect_left

n = int(sys.stdin.readline().rstrip())

data = list(map(int,sys.stdin.readline().split()))

arr =[]

for num in data:
    idx = bisect_left(arr,num)

    if idx == len(arr):
        arr.append(num)
    else:
        arr[idx] =num
print(len(arr))
    

