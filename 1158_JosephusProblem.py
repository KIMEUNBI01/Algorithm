# 백준 1158 김은비 

N, K = map(int, input().split()) #N명의 사람, 양의 정수 K
josephus = [i for i in range(1, N+1)] #1번부터 N번까지 원에 앉아 있는 N명의 사람들
result = [] #제거된 사람들
num = 0 #제거될 사람의 번호

while len(josephus) >0: 
    num = (num + (K-1)) % len(josephus)  
    result.append(str(josephus.pop(num))) #원에서 사람들이 제거되는 순으로 append
    
print("<%s>" %(", ".join(result)))