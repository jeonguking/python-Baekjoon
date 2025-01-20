s = input()
time =0
for item in s:
    asc = ord(item)
    if 80<= asc <=83:
         time += 8
    elif 84 <= asc <= 86:
         time +=9
    elif 87 <= asc <= 90:
         time += 10
    else:
        temp = (asc-65)//3
        time += temp+3
print(time)
