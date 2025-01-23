
n = int(input())

double = n*2

for i in range(double-1):
    if i <= n-1:
        for j in range(n-i-2,-1,-1):
            print(' ',end='')
        for k in range((2*(i+1))-1):
            print("*",end='')
    elif i > n-1 :
        for j in range(i-n+1):
            print(' ',end='')
        for k in range(2*(double-i-1)-1):
            print("*",end='')
    if i == double-2: break
    print("")



