# 백준 2293 김은비
'''
점화식: a[j] += a[j-i]
'''
n, k = map(int, input().split()) #동전종류, k원
c = [int(input()) for i in range(n)] #n개의 각기다른 동전의 가치

dp = [0 for _ in range(k+1)]
dp[0] = 1 #동전을 한개만 썼을 때

for i in c: #n개의 코인종류 모두 순회
    for j in range(i, k+1): #이전에 구했던 배열을 가져와 현재 종류의 코인을 더해 배열 넣어준다 
        if j-i >= 0 :
            dp[j] += dp[j-i]

print(dp[k])