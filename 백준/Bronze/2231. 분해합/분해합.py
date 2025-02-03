
n = int(input())

for num in range(n):
    k = [int(o) for o in str(num)]
    summ = sum(k) + num
    if  summ == n:
        print(num)
        exit()
print(0)
        


