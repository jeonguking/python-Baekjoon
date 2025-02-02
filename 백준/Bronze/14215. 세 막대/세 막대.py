data = list(map(int,input().split()))

data.sort()


while True:
    if data[0] + data[1] <= data[2]:
        data[2]-=1
    else :
        break
print(data[0]+data[1]+data[2])