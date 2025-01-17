n,m = input().split()

n = int(n)
m = int(m)

if m-45 < 0 :
    m +=15
    n -=1
    if n < 0 :
        n += 24
        print(f"{n} {m}")
    else:
        print(f"{n} {m}")
else :
    m-=45
    if n<0:
        n+=24
        print(f"{n} {m}")
    else:
        print(f"{n} {m}")
        

