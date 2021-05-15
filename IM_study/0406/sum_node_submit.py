T = int(input())
for tc in range(1, T+1):

    N, M, K = list(map(int, input().split()))

    TREE = [0 for i in range(N + 1)]

    for _ in range(M):
        node_id, node_item = list(map(int, input().split()))
        TREE[node_id] = node_item

    if N % 2 == 0:
        TREE[N // 2] = TREE[N]
        N -= 1

    while N > 1:
        TREE[N // 2] = TREE[N] + TREE[N - 1]
        N -= 2


    print("#{} {}".format(tc, TREE[K]))
