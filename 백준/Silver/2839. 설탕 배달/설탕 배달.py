n = int(input())

num = n


min = 100000

    
for num3 in range(10000):
    count = 1000000
    for num5 in range(10000):
        if (((num3 * 3) + (num5 * 5)) == n):
         
            count = num3 + num5
        elif (((num3 * 3 )+( num5 * 5) > n)) :
            break
    if min > count :
       
        min = count
if min == 100000:
    print(-1)
else : print(min)
