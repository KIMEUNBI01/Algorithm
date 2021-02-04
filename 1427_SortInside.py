# 백준 1427 김은비

### arr.sort() -> 원래의 리스트를 정렬된 상태로 변경 시킨다. [ 오름차순 - sort() / 내림차순 - sort(reverse=True) ] 
### sorted(arr) -> 정렬된 새로운 리스트를 반환한다. [ 오름차순 - sorted() / 내림차순 - sorted(reverse=True) ]

arr = list(map(int, input()))
arr.sort(reverse=True)
for i in arr:
    print(i, end='')