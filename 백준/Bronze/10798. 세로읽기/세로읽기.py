import sys


data = [list(sys.stdin.readline().rstrip()) for _ in range(5)]

string =""

for col in range(15):
    for row in range(5):
        t = len(data[row])
        if col < t :
             string += data[row][col]
print(string)


