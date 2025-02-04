
n = int(input())
num = 665
count = 0
while True:
    num+=1
    data = str(num)
    if '666' in data:
        count+=1
    if count == n:
        print(num)
        break




