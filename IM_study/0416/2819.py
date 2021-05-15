# 격자판의 숫자이어붙이기
# 7자리 숫자가 만들어지면 set에 추가해 중복을 제거1
# set의 크기를 출력
"""
아이디어 1
f(n, i, j)
if n == 7:

else:

visited도 필요 없고 확인만 하면 됨.


"""
di = 0, 0, -1, 1
dj = -1, 1, 0, 0
def find(i, j, n, s):
    if n == 7:
        t.add(s)
    else:
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if (ni >= 0 and ni < 4 and nj >=0 and nj<4):
                find(ni, nj, n+1, s+str[a[ni][nj]])



T = int(input())
for tc in range(1, T+1):
    a = [list(map(int, input().split())) for _ in range(4)]
    t = set()
    for i in range(4):
        for j in range(4):
            find(i, j, 0, '')
    print('#{} {}'.format(tc, len(t)))