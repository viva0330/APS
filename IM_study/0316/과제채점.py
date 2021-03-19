import sys
sys.stdin = open('과제채점.txt')
T  = int(input())
for tc in range(1, T+1):
    # N : 수강생의 수 K : 과제 제출한 사람의 수
    N, K = map(int, input().split())
    count = [0] * (N+1)
    student = list(map(int, input().split()))

    print()

    for i in range(K):
        count[student[i]] += 1
    # 0의 인덱스 번호찍기
    print('#{} '.format(tc), end="")
    for i in range(1, N+1):
        if count[i] == 0:
            print(i, end=" ")
    print()