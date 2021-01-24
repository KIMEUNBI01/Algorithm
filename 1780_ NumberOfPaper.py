# 백준 1780 김은비 

import sys

N = int(sys.stdin.readline()) #N(1 ≤ N ≤ 37, N은 3k 꼴)이 주어진다
Paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] #N개의 줄에 N개의 정수로 행렬이 주어진다

Minus = 0 #-1
Zero = 0 #0
Plus = 0 #1

def Cut(x, y, N) :
	global Minus, Zero, Plus
	check = Paper[x][y]
	for i in range(x, x+N): #N
		for j in range(y, y+N): #N
			if check != Paper[i][j]: #종이가 모두 같은 수로 되어 있지 않다면
				for k in range(3): #종이를 같은 크기의 9개의 종이로 자른다
					for l in range(3):
						Cut(x + k * N//3, y + l * N//3, N//3)
				return
			
	if check == -1: 
		Minus += 1
		return
	elif check == 0:
		Zero += 1
		return
	else: 
		Plus += 1
		return

Cut(0,0,N)
print(Minus) #-1로만 채워진 종이의 개수를 출력한다
print(Zero) #0로만 채워진 종이의 개수를 출력한다
print(Plus) #1로만 채워진 종이의 개수를 출력한다