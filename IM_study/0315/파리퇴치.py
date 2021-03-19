# import sys
# sys.stdin = open('파리퇴치_input.txt')
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M = list(map(int, input().split()))
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     sum_value = 0
#     for y in range(N):
#         for x in range(N):
#             sum_value = 0
#             for i in range(M):
#                 for j in range(i, i+M):
#                     sum_value += arr[i][j]
#     print(sum_value)

N, M = 7, 3
arr = [1, 8, 3, 6, 7, 11, 4]
max_value = 0

for i in range(N-M+1):
    sum_value = 0
    for j in range(i, i+M):
        sum_value += arr[j]
    if max_value < sum_value:
        max_value = sum_value
print(max_value)