# 백준 18258 김은비 

from collections import deque
import sys

def push(X):
    stack.append(X) #정수 X를 스택에 넣는다  
  
def pop():
    if len(stack) == 0:
        return -1 #만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다
    else:
        # pop()은 빼고 나머지 수를 앞으로 다시 옮길때 O(n)의 시간이 소요되기 때문에 deque로 구현하여 popleft()를 이용한다
        return stack.popleft() #아니면 스택에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다

def size():
	return len(stack) #스택에 들어있는 정수의 개수를 출력한다

def empty():
	if len(stack) == 0: #스택이 비어있으면 1을 출력한다 
		return 1
	else: #아니면 0을 출력한다
		return 0
        
def front():
    if len(stack) == 0: #만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다
        return -1
    else:
        return stack[0] #아니면 스택의 가장 앞에 있는 정수를 출력한다
        
def back():
    if len(stack) == 0: #만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다
        return -1
    else:
        return stack[-1] #아니면 스택의 가장 뒤에 있는 정수를 출력한다

N = int(input())
stack = deque([]) #pop()에서 popleft()함수를 사용하기 위해 deque로 구현한다

for _ in range(N):
	cmd = sys.stdin.readline().split() #타임에러를 피하기 위해 sys를 사용한다
	p = cmd[0]
	
	if p == "push":
		push(cmd[1])
	elif p == "pop":
		print(pop())
	elif p == "size":
		print(size())
	elif p == "empty":
		print(empty())
	elif p =="front":
		print(front())
	elif p =="back":
		print(back())
