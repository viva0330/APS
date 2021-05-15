def f(root):
    if root:
        # 얘가 비어있을때 트리가 아닐때 정수값 하나일때 어떻게 할지 고민해봐야함..!
        left_child = f(root.left)
        right_child = f(root.right)
        TREE[root] = left_child+right_child
        return left_child+right_child

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())



    for _ in range(M):
        leafnode, lst = list(map(int, input().split()))

    TREE = [0] * (N+1)

    # 보는 순서만 바꿔주면 됩니다.!
    # 순회하는 순서를 바꿔서 !
    # 기본 구조는 postorder 후위순회 써서
    # 채워나가는 방법도 있음,,!