n = int(input())

i = 1
num = 1
if n == 1 :
    print(1)
    exit()
while True:
    if ( n <= i*6+num):
        i+=1
        print(i)
        break
    num = i*6+num
    i+=1

