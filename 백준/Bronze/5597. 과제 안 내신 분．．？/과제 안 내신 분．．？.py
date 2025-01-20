data =[0 for _ in range(31)]

for _ in range(28):
    temp = int(input())
    data[temp] = temp

for i in range(1,31):
    if i != data[i]:
        print(i)
        
    
        

