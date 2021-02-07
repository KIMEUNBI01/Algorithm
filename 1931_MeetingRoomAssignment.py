# 백준 1931 김은비
'''
lambda (인자) : (리턴 값)  
이름이 없는 익명함수로 한번 쓰고 버리는 일회용 함수
key인자에 함수를 넘겨주면 그 함수의 반환값을 비교한뒤 순서대로 정렬한다
비교해야될 아이템의 요소가 여러개일 경우는 튜플로 순서를 지정해준다
'''

import sys

N = int(input()) #회의의 수
meeting = [list(map(int, input().split())) for _ in range(N)] #회의의 시작시간과 끝나는 시간
meeting.sort(key=lambda x: (x[1], x[0])) #회의가 끝나는 시간, 회의가 시작하는 시간을 오름차순으로 정렬

end = 0 #회의가 끝나는 시간 
count = 0 #최대 사용할 수 있는 회의의 최대 개수

for i in range(N):
    if meeting[i][0] >= end: #회의의 시작시간이 끝나는 시간보다 크거나 같으면
        end = meeting[i][1] 
        count += 1 #회의의 수 증가
            
print(count)