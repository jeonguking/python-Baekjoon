import sys

n,m = map(int,sys.stdin.readline().split())

data = []

for _ in range(n):
    data.append(list(sys.stdin.readline().rstrip()))

minn = 100000000


for i in range(n-7): # 밑으로 가는 반복문
    
    for j in range(m-7): # 옆으로 가는 반복문
       
        countW = 0 #W로 시작할때
        countB = 0 #B으로 시작할때

        #W인지 B인지 확인해서 카운트
        for row in range(8): 
            
            for col in range(8):

                if (row+col) %2 ==0 : # 짝수번째 바둑판일때
                    # +i , +j
                    if data[row+i][col+j] =='W':
                        countW+=1
                    if data[row+i][col+j] =='B':
                        countB+=1
                else : # 홀수번째 바둑판일때
                    if data[row+i][col+j] =='B':
                        countW+=1
                    if data[row+i][col+j] =='W':
                        countB+=1
        #최솟값 갱신
        cm = min(countB,countW)
        minn = min(minn,cm)
print(minn)

   

