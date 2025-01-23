n = int(input())
count = 0
for _ in range(n):
    s = input()
    data =list(s)
    result = []
    temp = 0
    for i in range(len(s)):
        if i == len(s)-1:
            if result.count(data[i]) != 0 :
                temp+=1
                break
            break

        if data[i] == data[i+1]:
            continue
        else :
            if result.count(data[i]) != 0 :
                temp+=1
                break
            result.append(data[i])
    if temp ==0 :
        count+=1
    
print(count)    
    