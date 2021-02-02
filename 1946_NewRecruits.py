#BOJ 1946 김은비

import sys

T = int(sys.stdin.readline()) #테스트 케이스의 개수

for _ in range(T):
    N = int(sys.stdin.readline()) #지원자의 수
    score = [] 

    for _ in range(N):
        score.append(list(map(int,sys.stdin.readline().split()))) #N명의 지원자의 서류심사 성적, 면접 성적의 순위 저장

    score.sort() #서류심사 성적을 기준으로 오름차순 정렬
    M = score[0][1] #서류심사 성적이 1등인사람의 면접점수가 기준 (서류심사 성적과 면접시험 성적 중 적어도 하나가 다른 지원자보다 떨어지지 않는 자만 선발한다는 원칙때문)
    count = 1 #선발할 수 있는 신입사원의 최대 인원수 (M이 기준이기 때문에 1부터 시작)

    for i in range(1, N):
        if score[i][1] < M: #M보다 면접 성적이 좋으면
            M = score[i][1] #M값 변경
            count += 1 #신입사원의 인원수 +1
    print(count)
