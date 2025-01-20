

n = int(input())

data1 = list(map(int,input().split()))

max_score = max(data1)
data2 = []
for i in data1:
    data2.append(i/max_score*100)

avg = sum(data2)/len(data2)

print(avg)
