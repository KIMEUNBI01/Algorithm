# 백준 2630 김은비 

import sys

N = int(sys.stdin.readline()) #전체 종이의 한 변의 길이
CP = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] #CP = ColoredPaper 
#색종이의 각 가로줄의 정사각형칸들의 색(하얀색으로 칠해진 칸은 0, 파란색으로 칠해진 칸은 1)

White = 0 #흰색
Blue = 0 #파란색

def Cut(x, y, N) :
    global Blue, White
    color = CP[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if color != CP[i][j]: #전체 종이가 모두 같은 색으로 칠해져 있지 않으면
                #똑같은 크기의 네 개의 N/2 × N/2색종이로 나눈다
                Cut(x, y, N//2) #1사분면
                Cut(x, y+N//2, N//2) #2사분면
                Cut(x+N//2, y, N//2) #3사분면
                Cut(x+N//2, y+N//2, N//2) #4사분면
                return
    if color == 0: #모두 흰색이라면
        White += 1
        return
    else: #아니면 모두 파란색이라면
        Blue += 1
        return

Cut(0,0,N)
print(White) #잘라진 햐얀색 색종이의 개수
print(Blue) #잘라진 파란색 색종이의 개수