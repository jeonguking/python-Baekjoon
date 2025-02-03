import sys

x1,y1,c,x2,y2,f = map(int,sys.stdin.readline().split())

for x in range(-999,1000,1):
    for y in range(-999,1000,1):
        if ((x1*x) + (y1*y) == c and (x2*x) + (y2 * y) == f):
            print(x,y)
            exit()
        
