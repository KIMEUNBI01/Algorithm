# 백준 1074 김은비 

N, r, c = map(int, input().split())
count = 0

def Z(n, x, y):
    global count
    if n == 1:
        print(2*x  +y)
        return
    if n == 2: #배열이 2*2가 되면 r행 c열을 찾아 몇번째로 방문했는지 출력하고 종료한다. 
        if x == r and y == c:  #1사분면
            print(count)
            return
        count += 1
        if x == r and y + 1 == c:  #2사분면
            print(count)
            return
        count += 1
        if x + 1 == r and y == c:  #3사분면
            print(count)
            return
        count += 1
        if x + 1 == r and y + 1 == c:  #4사분면
            print(count)
            return
        count += 1
    else: #배열을 Z모양으로 탐색하기 위해 배열이 2*2가 될 때까지 4등분 한 후에 재귀적으로 순서대로 방문한다
        Z(n/2, x, y)
        Z(n/2, x, y + n/2)
        Z(n/2, x + n/2, y)
        Z(n/2, x + n/2, y + n/2)

Z(2**N, 0, 0)