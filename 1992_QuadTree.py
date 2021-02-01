# 백준 1992 김은비 

N = int(input())
video = [list(map(int, input())) for _ in range(N)]
result = []

def quadtree(x, y, n):
    global result     

    for i in range(x, x + n):
        for j in range(y, y + n):
            if(video[i][j] != video[x][y]): #색이 다르면              
                result.append('(')
                quadtree(x, y, n//2) #1사분면
                quadtree(x, y + n//2, n//2) #2사분면
                quadtree(x + n//2, y, n//2) #3사분면
                quadtree(x + n//2, y + n//2, n//2) #4사분면
                result.append(')')       
                return
            
    result.append(str(video[x][y])) #모든 색이 같을 때

quadtree(0, 0, N)   
print(''.join(result))