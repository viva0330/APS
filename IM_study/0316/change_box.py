T = int(input())
for tc in range(1, T+1):
    # N : 상자의 개수 Q : 변경횟수
    N, Q = map(int, input().split())
    arr = [0 for _ in range(N)]
    print(arr)

    for i in range(Q):
        L, R = map(int, input().split())
        for j in range(L-1, R):
            arr[j] = i+1
    print('#{} '.format(tc), end="")
    print(*arr)