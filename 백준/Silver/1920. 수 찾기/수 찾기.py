import sys

n = int(sys.stdin.readline().rstrip())

datan = list(map(int,sys.stdin.readline().split()))


m = int(sys.stdin.readline().rstrip())

datam = list(map(int,sys.stdin.readline().split()))

datan.sort()
for i in range(len(datam)):
    temp = 0
    length = len(datan)-1
    start = 0
    while(start <= length):
        mid = (start+length)//2 #정수로 변환 소수점 버림
        if datan[mid] == datam[i]:
            print(1)
            temp = 1
            break
        elif datan[mid]> datam[i]:
            length = mid-1
        else:
            start = mid+1
    if temp == 0 :
        print(0)
    
