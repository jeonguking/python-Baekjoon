maxx = -10001
maxy = -10001
minx = 10001
miny = 10001

n = int(input())

for _ in range(n):
    a,b = map(int,input().split())
    if minx > a :
        minx = a
    if miny > b :
        miny = b
    if maxx < a:
        maxx = a
    if maxy < b :
        maxy = b
print((maxx-minx)*(maxy-miny))
    
        
