n = int(input())
i = 1
k = 0
r = 0
while True:
    r = k*(k+1)//2 #q이전까지의 합
    q = i*(i+1)//2
    if n <= q :
        break
    i+=1
    k+=1
result =""


if i % 2 ==0 :
    result = str(i-(q-n))+"/"+str(q-n+1)
else :
    result = str(q-n+1)+"/"+str(i-(q-n))
    

print(result)