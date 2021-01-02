# 백준 18238 김은비

string = list(input()) 

now = ord('A') #시작점
count = 0  #문자를 출력하는데 걸리는 시간

for i in string:
    start = ord(i) #입력된 문자열의 시작점

    right = now - start #오른쪽으로 돌아서 찾기
    left = start - now #왼쪽으로 돌아서 찾기

    if right < 0: #오른쪽으로 돌아서 찾은 값이 음수면 +26
        right += 26
    if left < 0: #왼쪽으로 돌아서 찾은 값이 음수면 +26
        left += 26

    if right <= left: #걸리는 시간의 최솟값 찾기
        count += right
    else:
        count += left

    now = ord(i) #다음 알파벳 계산을 위해 시작점 변경

print (count) 
