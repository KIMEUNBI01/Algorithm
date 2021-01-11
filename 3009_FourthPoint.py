# 백준 3009 김은비

X = [] #x축 좌표
Y = [] #y축 좌표

for i in range(3): #x,y 좌표쌍을 3개 입력받아 각각의 리스트에 append
    _x, _y = map(int, input().split())
    X.append(_x)
    Y.append(_y)
    
for i in X: #x좌표 구하기
    if X.count(i) == 1:  
        x = i
for i in Y: #y좌표 구하기
    if Y.count(i) == 1:
        y = i

print(x,y)
