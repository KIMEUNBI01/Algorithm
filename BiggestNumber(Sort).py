# programmers 가장 큰 수 김은비

def solution(numbers):
    result = [] #가장 큰 수를 저장할 리스트 
    
    for n in numbers: 
        number = str(n) #원소 n
        add = list(str(n)) #원소 n을 4자리로 만들 리스트 

        #numbers의 원소는 0 이상 1,000 이하이기 때문에 정수를 모두 4자리로 만든다
        i = 0
        while len(add) < 4:
            add.append(number[i]) 
            i = (i + 1) % len(number)
            
        add = int("".join(add)) #int형으로 바꾼다       
        result.append([add, number]) #[nnnn, n]

    result = sorted(result, reverse = True) #앞에서 구한 값을 바탕으로 큰 수 부터 정렬한다
    
    return str(int("".join(res[1] for res in result))) #정렬한 값을 순서대로 출력한다
