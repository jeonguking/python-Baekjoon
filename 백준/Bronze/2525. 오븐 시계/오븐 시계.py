n,m = input().split()
t = int(input())
n = int(n)
m = int(m)

m += t
n += m//60

m %= 60

if n >=24 :
    n %= 24 



print(f"{n} {m}")
        

