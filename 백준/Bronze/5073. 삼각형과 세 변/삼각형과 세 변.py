import sys
while True:
    
    a,b,c = map(int,sys.stdin.readline().split())
    if a==b==c==0:
        break
    data =[]
    data.append(a)
    data.append(b)
    data.append(c)
    data.sort()
    if data[0]+data[1] <= data[2]:
        print("Invalid")
        continue
    if a==b==c:
        print("Equilateral")
        continue
    if a==b or a==c or b==c :
        print("Isosceles")
        continue
    if a!=b!=c:
        print("Scalene")
        continue
    
    
