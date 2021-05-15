import sys
sys.stdin = open('5188_sample_input.txt')
# 중간 중간 움직이면서 거리가 필요.
# 중간값에 대한 거리가 필요
def find(row, col, mid_value):
    global min_value
    # 이미 들어간다면..

    if row == N-1 and col == N-1:
        # 지금까지 온 것 중에 최소값
        if min_value > mid_value:
            min_value = mid_value
        return

    if col+1 < N:
        find(row, col+1, mid_value+arr[row][col+1])
    if row+1 < N:
        find(row+1, col, mid_value+arr[row+1][col])


T = int(input())
for tc in range(1, T+1):
    # N : 칸
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]