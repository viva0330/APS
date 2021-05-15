# i => X
def dijk(s):
    D[s] = 0
    curV = s

    for i in range(N + 1):
        # D가 min 인 curV를 결정
        minV = 1e10
        for i in range(N+1):
            if i in U : continue
            if minV > D[i]:
                minV = D[i]
                curV = i
        U.append(curV)
        # curV를 사용하여 인접한 노드의 D를 업데이트
        for i in range(1, N+1):
            if i in U: continue
            if G[i][curV]:
                # x에서 돌아오는 것에 대한 이야기.
                D[i] = min(D[i], D[curV] + G[curV][i])

# X->i
def dijk(s):
    D[s] = 0
    curV = s

    for i in range(N + 1):
        # D가 min 인 curV를 결정
        minV = 1e10
        for i in range(N+1):
            if i in U : continue
            if minV > D[i]:
                minV = D[i]
                curV = i
        U.append(curV)
        # curV를 사용하여 인접한 노드의 D를 업데이트
        for i in range(1, N+1):
            if i in U: continue
            if G[curV][i]:
                # x에서 돌아오는 것에 대한 이야기.
                D[i] = min(D[i], D[curV] + G[curV][i])

T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int, input().split())
    G = [[0] * (N+1) for _ in range(N+1)]

    for i in range(M):
        x, y, c = map(int, input().split())
        G[x][y] = c

    D = [1e10] * (N + 1)
    U = []

    dijk(X)