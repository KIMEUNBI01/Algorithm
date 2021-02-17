# 백준 11726 김은비
'''
점화식 a[i] = a[i-1] + a[i-2]
'''
n = int(input()) #2×n 직사각형의 'n'
tile = [0, 1, 2] #tile[1]과 tile[2]는 미리 구해둔다

for i in range(3, n+1): #tile[3]부터는 점화식을 이용해서 계산
    tile.append( tile[i - 1] + tile[i - 2] )

print(tile[n] % 10007) #2×n 크기의 직사각형을 채우는 방법의 수를 10007로 나눈 나머지를 출력