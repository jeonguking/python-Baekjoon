s = input()

count = 0
i = 0 
while(i < len(s)):
    if i == len(s)-1:
        count+=1
        break
    if s[i] == 'c' and (s[i+1] == '=' or s[i+1] == '-'):
        count+=1
        i+=2
        continue
    elif s[i] == 'd':
        if s[i+1] == '-':
            count+=1
            i+=2
            continue
        elif s[i+1] == 'z':
            if i+1 != len(s)-1:
                if s[i+2] == '=':
                    count+=1
                    i+=3
                    continue
    elif s[i] == 'l' and s[i+1] == 'j':
        count+=1
        i+=2
        continue
    elif s[i] == 's' and s[i+1] == '=':
        count+=1
        i+=2
        continue
    elif s[i] == 'z' and s[i+1] == '=':
        count+=1
        i+=2
        continue
    elif s[i] == 'n' and s[i+1] == 'j':
        count+=1
        i+=2
        continue
    i+=1
    count+=1
print(count)