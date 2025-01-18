import sys
from collections import deque 
data = int(sys.stdin.readline().rstrip())

dq = deque()
count =0
temp = data
while True:
    if temp //10 != 0:
        count +=1
    else :
        break
    temp /= 10
count+=1

num1 = 0
num2 = 0

for i in range(1,count+1):
    if i <= count/2:
        num1 += data % 10
    else:
        num2 += data % 10 
    data //= 10

if num1 == num2:
    print("LUCKY")
else:
    print("READY")





