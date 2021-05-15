# 중위,,?


def tr(root):
    global value
    if root <= N:
        tr(root*2)
        tree[root] = value
        value += 1
        tr(root*2 + 1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)

    # 시작점 데이터 1부터 채우기로 되어이씅ㅁ
    value = 1
    tr(1)
    # 루트의 저장된 값과  N//2에 저장된 값
    print('#{} {} {}'.format(tc, tree[1], tree[N//2]))

# 주의해야할 것 노드 번호고 우리가 해야할 건 데이터 채우기!
# 데이터가 아직 안 채워져있는 트리를 만들어야합니다 그래서 tree를 만들엇죠,,?
# 만들어져있는 것을 기준으로 맨 왼쪽부터 데이터 채움
# 이게 데이터 순회
# 왼쪽 보고 가운데보고 그리고 오른쪽보고! inorder순회 사용하면 됨
# 오 생각 자체는 틀리지 않은 듯 해~
# 트리 만들고 중위순회하면서 데이터를 채운다,,!
