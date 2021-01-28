# 백준 7568 김은비 

N = int(input())
People = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    rank = 1
    for j in range(N):
        #키와 몸무게 두 값이 모두 큰 경우만 큰 덩치이다
        if People[i][0] < People[j][0] and People[i][1] < People[j][1]:
                rank += 1
    print(rank, end = " ")