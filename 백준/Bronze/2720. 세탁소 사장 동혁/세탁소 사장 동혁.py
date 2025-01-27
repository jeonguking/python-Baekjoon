n = int(input())
data = [25,10,5,1]
for _ in range(n):
    k = int(input())

    for i in data:
        num = k // i
        k %= i
        print(num,end=' ')
    print('')