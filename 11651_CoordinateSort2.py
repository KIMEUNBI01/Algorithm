# 백준 11651 김은비

import sys

N = int(sys.stdin.readline()) #점의 개수

coordinate = [] 
for _ in range(N): #i번점의 위치 xi와 yi를 순서를 바꿔 coordinate에 append
    x, y = map(int, sys.stdin.readline().split())
    coordinate.append([y, x])
    
coordinate.sort() #좌표를 y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순서로 정렬

for i in range(N):
    print(coordinate[i][1], coordinate[i][0])