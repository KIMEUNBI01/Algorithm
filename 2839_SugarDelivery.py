# 백준 2839 김은비

Bag = 0 # 필요한 봉지의 개수
Kg = int(input()) # 설탕의 무게

while Kg >= 0: # 설탕의 무게가 0 이상이면
    if (Kg % 5) == 0: # 5의 배수이면
        Bag += Kg // 5 # 5로 나눈 몫을 구하고
        print(Bag) # 필요한 봉지의 개수 출력
        break
    # 5의 배수가 될 때까지
    Kg -= 3 # 설탕-3
    Bag += 1 # 봉지+1
else: 
    print("-1")
