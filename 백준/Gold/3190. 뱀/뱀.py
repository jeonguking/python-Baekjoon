import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

applenum = int(sys.stdin.readline().rstrip())

count = 0

#초기화
data = [[0 for _ in range(n+1)] for _ in range(n+1)]

#사과 입력받기
#사과가 있는곳은 2
for i in range(applenum):
    a,b = map(int,sys.stdin.readline().split())
    data[a-1][b-1] = 2

#벽은 n
wall = n
#뱀의 방향 변환 횟수
l = int(sys.stdin.readline().rstrip())

#숫자
number = deque()
#방향
way = deque()

for _ in range(l):
    a,b = sys.stdin.readline().split()
    a = int(a)
    number.append(a)
    way.append(b)

snake = deque()

time = 0
#첫번쨰 칸 1로 1은 뱀
data[0][0] = 1
snake.append([0,0])

lastx,lasty = 0,0
direct = 'R'



for i in range(l+1):
    
    if i != l:
        num = number.popleft()    
    else :
        num = 10000
        
    
    #첫번 째 시도는 무조건 오른쪽
    if i == 0 :
        for j in range(1,num+1):
            time +=1
            if data[0][j] == 2:
                data[0][j] = 0
            else : 
                snake.popleft()
            snake.append([0,j])
            lastx,lasty = 0,j   
        
        
        continue
    
    direction = way.popleft()
    if direction == 'D':
        #오른쪽일떄
        if direct == 'R' :
            direct = 'D'
        #아래일때
        elif direct =='D':
            direct = 'L'
        #왼쪽일때
        elif direct == 'L':
            direct = 'U'
        #위일때
        elif direct == 'U':
            direct = 'R'
    
    else :    
        #오른쪽일떄
        if direct == 'R' :
            direct = 'U'
        #아래일때
        elif direct =='D':
            direct = 'R'
        #왼쪽일때
        elif direct == 'L':
            direct = 'D'
        #위일때
        elif direct == 'U':
            direct = 'L'    
    
    



    if direct == 'R':
        x,y = lastx,lasty
        
        for col in range(y+1,10000):
            #디버깅
            

            if snake.count([x,col]) != 0:
                time+=1
                print(time)
                exit()
            if col == n :
                time+=1
                print(time)
                exit()
            if data[x][col] == 2 :
                data[x][col] =0
            else :
                snake.popleft()
            snake.append([x,col])
            lastx,lasty = x,col
            
            time+=1
            if time == num :
                break
            
            
             
        

    elif direct =='D':
        x,y = lastx,lasty

        for row in range(x+1,10000):
            

            if snake.count([row,y]) != 0:
                time+=1
                print(time)
                exit()
            if row == n :
                time+=1
                print(time)
                exit()

            if data[row][y] == 2 :
                data[row][y] =0
            else :
                snake.popleft()
            snake.append([row,y])
            lastx,lasty = row,y 
            
            time+=1
            
            if time == num :
                break
            
            
           
        
        
    elif direct == 'L':
        x,y = lastx,lasty
        
        for col in range(y-1,-10000,-1):
            #디버깅
            
            if snake.count([x,col]) != 0:
                time+=1
                print(time)
                exit()
            if col < 0 :
                time+=1
                print(time)
                exit()
            if data[x][col] == 2 :
                data[x][col] =0
            else :
                snake.popleft()
            snake.append([x,col])
            lastx,lasty = x,col
            
            time+=1
           
            if time == num :
                break
            
           
            
             
            
        
    else:
        x,y = lastx,lasty
        
        for row in range(x-1,-1000,-1):
            #디버깅
            
            if row < 0 :
                time+=1
                print(time)
                exit()
            if snake.count([row,y]) != 0:
                time+=1
                print(time)
                exit()
            if data[row][y] == 2 :
                data[row][y] =0
            else :
                snake.popleft()

            
            snake.append([row,y])
            
            lastx,lasty = row,y
            
            time+=1
          
            if time == num :
                break

            

