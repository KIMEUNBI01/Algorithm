# 백준 11399 김은비 

n = int(input())
arr = list(map(int, input().split()))

#누적시간을 구하는 문제이므로 정렬을 한 후 계산하면 더욱 쉬움 
arr.sort()
num = 0

for i in range(n):
    for j in range(i+1):
        num += arr[j] #누적시간 계산 

print(num)
