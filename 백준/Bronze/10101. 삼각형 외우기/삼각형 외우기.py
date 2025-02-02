a = int(input())
b = int(input())
c = int(input())

if a==b==c==60 :
    print("Equilateral")
    exit()
if (a+b+c) == 180 and (a == b or b == c or a == c):
    print("Isosceles")
    exit()
if (a+b+c) == 180 and (a!=b!=c):
    print("Scalene")
    exit()
print("Error")