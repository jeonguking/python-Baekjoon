
while True:
    n = int(input())
    if n == -1:
        break
    sum = 0
    line = f"{n} = "
    for i in range(1,n):
        if n % i == 0 :
            line += f"{i} + "
            sum += i
            
    if n == sum :
        print(line[:-2])
    else :
        print(f"{n} is NOT perfect.")