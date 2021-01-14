# 백준 10828 김은비 

import sys

def push(X):
    stack.append(X) #정수 X를 스택에 넣는다  
		
def pop():
	if len(stack) == 0:
		return -1 #만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다 
	else:
		return stack.pop() #스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다
	
def top():
	try:
		return stack[-1] #스택의 가장 위에 있는 정수를 출력한다
	except:
		return -1 #만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다
	
def empty():
	if len(stack) == 0: #스택이 비어있으면 1을 출력한다 
		return 1
	else: #아니면 0을 출력한다
		return 0
	
def size():
	return len(stack) #스택에 들어있는 정수의 개수를 출력한다


N = int(input())
stack = []
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
	elif p == "top":
		print(top())
