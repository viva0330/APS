import sys
sys.stdin = open('subtree_sample_input.txt')

def tr(root):
    global cnt
    if root:
        cnt += 1
        tr(Tree[root][0])
        tr(Tree[root][1])

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())

    lst = list(map(int, input().split()))
    Tree = [[0, 0] for _ in range(E+2)]
    # 트리 만드는 과정
    for i in range(0, len(lst), 2):
        p = lst[i]
        c = lst[i+1]
        if Tree[p][0] == 0:
            Tree[p][0] = c
        else:
            Tree[p][1] = c

    cnt = 0
    tr(N)
    print('#{} {}'.format(tc, cnt))