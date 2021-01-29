N, M = map(int, input().split())
Card = list(map(int,input().split()))
BlackJack = []

#3장의 카드를 뽑아 모든 경우의 수를 살펴보기 위해 3중 for문을 이용한다
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            if Card[i]+Card[j]+Card[k] <= M: #세 카드의 합이 M보다 작을 경우
                BlackJack.append(Card[i]+Card[j]+Card[k]) #BlackJack 배열에 append
                
print(max(BlackJack)) #BlackJack 배열 중 max 값을 출력하면 그 값이 M 또는 M에 가장 가까운 값이다