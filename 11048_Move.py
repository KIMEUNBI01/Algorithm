# 백준 11048 김은비
'''
점화식: b[i][j] = a[i-1][j-1] + max( b[i-1][j], b[i-1][j-1], b[i][j-1])
'''
N, M = map(int, input().split())
Maze = [list(map(int, input().split())) for _ in range(N)]

Candy = [[0]*(M+1) for _ in range(N+1)] #모든칸(가장 위, 가장 왼쪽)을 탐색하기 위해 칸을 늘려준다

for i in range(1, N+1): #점화식을 이용하여 준규가 (N, M)으로 이동할 때, 가져올 수 있는 사탕 개수를 구한다
    for j in range(1, M+1):
        Candy[i][j] = Maze[i-1][j-1] + max( Candy[i-1][j], Candy[i-1][j-1], Candy[i][j-1] )

print(Candy[-1][-1]) #Candy[N][M]