# 백준 1343 김은비

import sys

Board = sys.stdin.readline().rstrip("\n") #보드판
Polyomino = Board.split(".") #'.'는 폴리오미노로 덮으면 안 된 '.'을 기준으로 나눈다
result = []
res = 0

for i in Polyomino:
	lengh = len(i)
	if lengh >= 4 and lengh%2 == 0: #split한 Polyomino의 길이가 4보다 크거나 같고 2로 나눠 떨어지는 경우
		result.append("AAAA"*(lengh//4) + "BB"*((lengh%4)//2)) #길이를 4로 나눈 몫만큼은 "AAAA", 그리고 남은 나머지를 2로 나눈 몫만큼은 "BB"를 append한다
		result.append(".") #split을 했기 때문에 "."도 같이 append 해준다
		
	elif lengh%2 == 0: #split한 Polyomino의 길이가 2로만 나눠 떨어지는 경우
		result.append("BB"*(lengh//2)) #길이를 2로 나눈 몫만큼 "BB"를 append한다
		result.append(".") #split을 했기 때문에 "."도 같이 append 해준다
		
	else: #split한 Polyomino의 길이가 홀수인 경우
		res = -1 # -1을 출력하기 위해 res를 -1로 바꾼다
		break

if res == -1:
	print(-1) #덮을 수 없으면 -1을 출력한다
else:
	del result[-1] #위에서 덮을 때 마다 끝에 "."을 append해 줬기 때문에 마지막 덮은 Polyomino는 "."을 제거한다
	for i in range(len(result)):
		print(result[i], end="") #줄바꿈 없이 출력한다