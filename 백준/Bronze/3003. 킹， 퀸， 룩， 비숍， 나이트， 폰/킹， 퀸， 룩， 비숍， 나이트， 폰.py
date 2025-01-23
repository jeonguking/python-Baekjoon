data = [1,1,2,2,2,8]

input = list(map(int,input().split()))
result =[0 for _ in range(6)]
for i in range(6):
    result[i] = data[i]-input[i]

print(*result)