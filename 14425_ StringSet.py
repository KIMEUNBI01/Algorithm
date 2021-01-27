# 백준 14425 김은비 

import sys

N, M = map(int, sys.stdin.readline().split())
S = [sys.stdin.readline() for i in range(N)] #집합 S에 포함되어 있는 N개의 문자열
Str = [sys.stdin.readline() for j in range(M)] #검사해야 하는 M개의 문자열 
count = 0

for k in range(M):
    if Str[k] in S: #집합 Str에 집합 Sdp 포함되어 있는 문자열과 같은 문자열이 있으면
        count += 1 #count +1
print(count)