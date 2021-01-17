# 11866 백준 김은비

#1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다
N, K = map(int, input().split())
stack = [i for i in range(1, N+1)]
Num = 0

#result = (N, K)-요세푸스 순열 
result = []

#순서대로 K번째 사람을 제거한다 
# 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다
# 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다
while len(stack) > 0:
    Num = (Num+k-1) % len(stack) #K번째 사람
    result.append(stack.pop(Num))

print('<'+', '.join(map(str, result))+'>')
