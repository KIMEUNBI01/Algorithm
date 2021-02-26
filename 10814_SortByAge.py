# 백준 10814 김은비

import sys

N = int(sys.stdin.readline()) #온라인 저지 회원의 수
member = [] #N명의 회원들의 나이와 이름을 저장할 배열 

for i in range(N):
    member.append(list(sys.stdin.readline().split())) #N명의 회원들의 나이와 이름을 저장
    
member.sort(key=lambda x: int(x[0])) #회원들을 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬

for i in range(N):
    print(member[i][0], member[i][1]) #정렬한 회원을 나이, 이름 순으로 출력