import sys
sys.stdin = open('5189_sample_input.txt')

# 순열을 구하는게 제일 중요..!
# 순열을 구하는 알고리즘 필요..!
def cal(lst):
    # 0 1 2
    for i in range(len(lst)-1):
        s = lst[i]
        e = lst[i+1]
        sum_value += arr[s][e]
        # 근데 우리가 구하고 싶은건 012 0
        sum_value = sum_value + arr[e][0]
        return sum_value

def perm(k, s, mid_value):
    global min_value
    if min_value < mid_value:
        return
    # 내가 원하는 순열 갯수 N개에 도달했을 때
    """
        if k == N:
        mid_value = cal(lst)
        if min_value > mid_value:
            min_value = mid_value
        return min_value
    """
    if k == N :
        mid_value += arr[s][0]
        if min_value > mid_value:
            min_value = mid_value
        return min_value

    for i in range(1, N):
        if not visited[i]:
            lst[k] = i
            visited[i] = True


            perm(k+1, i, mid_value + arr[s][i])
            visited[i] = False

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * (N+1)
    # 1231 -> 0120
    lst[0] = 0
    visited[0] = True
    perm(1)
