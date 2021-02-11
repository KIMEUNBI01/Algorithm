# 백준 1541 김은비

before = input().split('-') #주어진 식을 '-'를 기준으로 숫자를 split해서 입력받는다
result = 0  #최소값 저장

for i in before[0].split('+'): #'-'가 나오기 전까지 전부 더해준다
    result += int(i) 

for j in before[1:]: #배열의 1번부터
    for k in j.split('+'): #'+'가 나오면 전부 빼 result에 저장한다
        result -= int(k) 
        
print(result)