from collections import deque

N = int(input())
stack = deque([i for i in range(1, N+1)])

while len(stack) > 1:
    #제일 위에 있는 카드를 버린다
    stack.popleft()
    #제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다
    MoveNum = stack.popleft()
    stack.append(MoveNum)

#제일 마지막에 남게 되는 카드를 출력한다    
print(stack[0])