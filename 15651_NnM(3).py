# 백준 15651 김은비

N, M = map(int, input().split())
Num = [] #수열을 담아둘 배열

def DFS(x, N, M): 
    if(x == M): #1부터 N까지 자연수 중에서 중복을 허용하여 M개를 고른 수열을 오름차순으로 출력한다 
        print(*Num)
        return
    
    for i in range(N): 
        Num.append(i+1) #그리고 Num에 i+1을 append (인덱스는 0부터 시작하기 때문에 숫자를 구하기 위해선 1을 늘려준다)
        DFS(x+1, N, M) #다음 깊이를 탐색한다
        Num.pop() #사용한 배열은 지워준다
            
DFS(0, N, M)