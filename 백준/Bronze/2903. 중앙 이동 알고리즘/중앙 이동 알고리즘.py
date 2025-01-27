n = int(input())
num = 0
dot = 3

for i in range(n):
    if i != 0:
        dot += (dot-1)
        num = dot**2
    else :
        num = 9
print(num)
