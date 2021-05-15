# x번 집에서 각자의 집으로 돌아가는 경우
# -> x를 시작정점으로 하는 다익스트라 알고리즘 적용
# x번으로 모이는 것은
# x로 진입하는 비용을 기준으로 다익스트라 알고리즘
#  2회만 적용해 해결.
def dij(N, X, adj, d):
    for i in range(N+1): # 출발지로부터의 비용
        d[i] = adj[X][i]
    v = [0] * (N+1)
    v[X] = 1 # 출발지 비용 확정
    for _ in range(N-1): # 남은 노드 고려
        minldx = 0
        for i in range(1, N+1):
            if v[i] == 0 and d[i] < d[minldx]: # 남는 노드 중 비용이 최소
                minldx = i
            v[minldx] = 1 # 비용 결정
            for i in range(1, N+1): #minidx에 인접인 노드에 대해
                if minldx != i and adj[minldx][i] < 1000000:
                    d[i] = min(d[i], d[minldx]+adj[minldx][i])


T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int, input().split())
    adj1 = [[1000000] * (N+1) for i in range(N+1)] # 진출기준
    adj2 = [[1000000] * (N + 1) for i in range(N + 1)] # 진입기준

    for i in range(N+1): # 출발==도착, 비용 0
        adj1[i][i] = 0
        adj2[i][i] = 0

    for _ in range(M):
        u, v, w = map(int, input().split())
        adj1[u][v] = w
        adj2[u][v] = w
    d1 = [1000000]*(N+1)
    d2 = [1000000]*(N+1)
    dij(N, X, adj1, d1)
    dij(N, X, adj2, d2)

    maxV = 0
    for i in range(1, N+1): # 모두 이동이 가능, 무한대는 없다.
        if d1[i] + d2[i] > maxV:
            maxV = d1[i]+ d2[i]
    print('#{} {}'.format(tc, maxV))