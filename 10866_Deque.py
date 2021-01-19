# 백준 10866 김은비 

import sys

def push_front(X):
	Deque.insert(0,X) #정수 X를 덱의 앞에 넣는다

def push_back(X):
	Deque.append(X) #정수 X를 덱의 뒤에 넣는다
    
def pop_front():
	if len(Deque) == 0: #덱에 들어있는 정수가 없는 경우에는 -1을 출력한다
		return -1
	else: #아니면 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다
		return Deque.pop(0) 
        
def pop_back():
	if len(Deque) == 0: #덱에 들어있는 정수가 없는 경우에는 -1을 출력한다
		return -1
	else: #덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다
		return Deque.pop() 

def size():
	return len(Deque) #덱에 들어있는 정수의 개수를 출력한다

def empty():
	if len(Deque) == 0: #덱이 비어있으면 1을 출력한다 
		return 1
	else: #아니면 0을 출력한다
		return 0
        
def front():
	if len(Deque) == 0: #만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다
		return -1
	else:
		return Deque[0] #아니면 덱의 가장 앞에 있는 정수를 출력한다
        
def back():
	if len(Deque) == 0: #만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다
		return -1
	else:
		return Deque[-1] #아니면 덱의 가장 뒤에 있는 정수를 출력한다

N = int(input())
Deque = []

for _ in range(N):
	cmd = sys.stdin.readline().split() #타임에러를 피하기 위해 sys를 사용한다
	p = cmd[0]
	
	if p == 'push_front':
		push_front(cmd[1])
	elif p == 'push_back':
		push_back(cmd[1])
	elif p == 'pop_front':
		print(pop_front())
	elif p == 'pop_back':
		print(pop_back())
	elif p == "size":
		print(size())
	elif p == "empty":
		print(empty())
	elif p =="front":
		print(front())
	elif p =="back":
		print(back())  