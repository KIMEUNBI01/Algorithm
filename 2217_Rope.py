# 백준 2217 김은비

N = int(input()) #정수 N
rope = [int(input()) for _ in range(N)] #N개의 각 로프가 버틸 수 있는 최대 중량
    
rope.sort(reverse = True) #내림차순 정렬

MaxWeight = []
for i in range(N):
    MaxWeight.append(rope[i] * (i+1)) #(N번째 로프의 길이 * N)

print(max(MaxWeight))