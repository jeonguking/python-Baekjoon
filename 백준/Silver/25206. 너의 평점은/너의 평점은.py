import sys

result = 0
score =0
sum = 0
for _ in range(20):
    input = list(sys.stdin.readline().split())    
    if input[2] != 'P':
        sum += float(input[1])
    if input[2] == 'A+':
        score+= float(input[1]) * 4.5 
    elif input[2] == 'A0':
        score+= float(input[1]) * 4.0
    elif input[2] == 'B+':
        score+= float(input[1]) * 3.5
    elif input[2] == 'B0':
        score+= float(input[1]) * 3.0
    elif input[2] == 'C+':
        score+= float(input[1]) * 2.5
    elif input[2] == 'C0':
        score+= float(input[1]) * 2.0
    elif input[2] == 'D+':
        score+= float(input[1]) * 1.5
    elif input[2] == 'D0':
        score+= float(input[1]) * 1.0
    elif input[2] == 'F':
        score+= 0
result = score/sum
print(result)