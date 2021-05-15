arr = [
    [4, 4, 3, 2, 1], [2, 2, 1, 6, 5], [3, 5, 4, 6, 7], [4, 2, 5, 9, 7], [8, 1, 9, 5, 6]
]

# 위치(행, 열) 크기를 입력받아 합을 구하여라,
R, C, size = int(input().split())

# 2, 1, 2
# 1, 4, 3

# 가로 세로 위치 따질 때 배열은 0부터 시작! 0부터 볼거냐 1부터 볼꺼냐 주의깊게 봐야할 것.
# 위치 계산하는 거 생각하고..!
# 시작점을 기분으로 해서 2, 1

# start 지점과 end지점하고 계산
# 방법 1
s =
e =
for i in range(s, e):
    sum_value += arr[r][i]

s =
e =
for i in range(s, e):
    sum_value += arr[i][c]

# 방법 2
for i in range(size):
    #  경계체크 주의!
    sum_value += arr[r][c+i]

for i in range(size);
#   경계 체크
    sum_value += arr[r+i][c]

# 방법 3 델타사용하기!
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(크기):
    for j in range(4):
#         경계체크
        newR =
        newC =
        sum_value += arr[newR][newC]

