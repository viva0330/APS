# 공장
# 순열, 최소비용!
# 백트래킹 가능

def dfs(idx, sum_value):
    global answer
    if sum_value >= answer:
        return
    if idx == N:
        answer = sum_value
    for i in range(N):
        if visited[i]:
            visited[i] = 0
            dfs(idx+1, sum_value + V[idx][i])
            visited[i] = 1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    V = [list(map(int, input())) for _ in range(N)]
    visited = [1 for _ in range(N)]
    answer = 99999
    dfs(0, 0)
    print('#{} {}'.format(tc, answer))

"""
def per(k, midV):
    if k == N:
        return 
    if midV > minV:
        return 
    
    for i in range(N):
        if not visited[i]:
            lst[k] = i
            visited[i] = True
            per(k+1, midV + arr[k][i])
            visited[i] = False
"""
