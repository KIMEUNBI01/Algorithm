# 백준 11650 김은비

import sys

N = int(sys.stdin.readline()) #점의 개수

coordinate = [] #i번점의 위치 xi와 yi를 저장할 배열 
for _ in range(N):
    coordinate.append(list(map(int, sys.stdin.readline().split()))) #i번점의 위치 xi와 yi를 coordinate에 append
    
coordinate.sort() #좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬

for i in range(N):
    print(coordinate[i][0], coordinate[i][1])