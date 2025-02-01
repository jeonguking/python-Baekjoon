a,b,v = map(int,input().split())
result = (v-b-1)/(a-b)
if isinstance(result,int):
    print(int(result))
else :
    print(int(result+1))


