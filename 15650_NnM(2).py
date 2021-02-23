# 백준 15650 김은비

N, M = map(int, input().split())
Check = [False]*N #중복되는 수열을 없애기 위한 배열
Num = [] #수열을 담아둘 배열


def DFS(x, y, N, M): 
    if(x == M): #1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열을 오름차순으로 출력한다
        print(*Num)
        return
    
    for i in range(y, N):
        if not Check[i]: #아직 담지 않았다면
            Check[i] = True #False인 i를 True로 변경한다
            Num.append(i+1) #그리고 Num에 i+1을 append (인덱스는 0부터 시작하기 때문에 숫자를 구하기 위해선 1을 늘려준다)

            DFS(x+1, i+1, N, M) #중복을 피해 다음 깊이을 탐색한다
            Check[i] = False #모든 경우를 탐색하기 위해 True인 i를 다시 False로 변경한다
            Num.pop() #사용한 배열은 지워준다
            
DFS(0, 0, N, M)