import sys

n = int(sys.stdin.readline())
data =[]
for i in range(n):
    a,b = sys.stdin.readline().split()
    data.append([int(a),b,i])

sorted_data = sorted(data,key=lambda x:(x[0],x[2]))

print('\n'.join([f'{i} {j}' for i,j,_ in sorted_data]))


