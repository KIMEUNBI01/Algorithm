# 백준 10773 김은비 

N = int(input())
s = []

for i in range(N):
    Num = int(input())
    if Num == 0: #입력받은 숫자가 0이면 삭제
        s.pop()
    else: #아니면 추가
        s.append(Num)
            
print(sum(s)) #sum함수를 이용하여 리스트의 전체합 출력
