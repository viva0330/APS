# 최소 교환 횟수
# 부분집합 문제,,!
# 넣는경우 전부 다 안 넣는 경우...


def dfs(idx, _sum):
    global answer
    if answer < _sum: return
    if idx >= N:
        answer = _sum
        return
    count = station[idx]
    for i in range(count, 0, -1):
        dfs(idx + i, _sum + 1)


for t in range(int(input())):
    answer = float('inf')
    station = list(map(int, input().split()))
    # 0부터 시작하니까 -1
    N = station.pop(0) - 1
    # 처음 충전은 안치니까 -1로 시작해서 보정해주기
    dfs(0, -1)
    print('#{} {}'.format(t + 1, answer))


"""
def chk():
    # 갈 수 있는지 없는지 확인

def find(k):
    if k == N:
        if cnt < minV:
            minV = cnt
        return
    if cnt > minV
        return 
    
    if remain == 0
        return 
    
    # tmp[k] = 0
    find(k+1, remain-1, cnt)
    # tmp[k] = 1
    find(k+1, lst[k+1], cnt+1)

tmp[0] = 1
find(1,)


"""
