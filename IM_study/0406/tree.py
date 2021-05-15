# 재귀를 이용하여 트리를 순회!
# 재귀를 이용해서 순회를 할 때 가장 기본적인 것
"""
def f(root):
    root 처리
    f(root.left)
    f(root.right)


def f(root):
    if base:
        root 처리
    if 왼쪽에 트리가 있으면
        f(root.left)
    if 오른쪽에 트리가 있으면
        f(root.right)


def f(root):
    if base : # 왼쪽 오른 쪽 없는 경우
        return root의 값
    if root 왼쪽에 트리가 있으면 # TREE[root][0]: , TREE[root*2]
        f(root.left)
    if root 오른쪽에 트리가 있으면 #TREE[root][1]:
        f(root.right)
    if base:
    root 처리


def f(root):
    if base : # 왼쪽 오른 쪽 없는 경우
        return root의 값
    if root 왼쪽에 트리가 있으면 # TREE[root][0]: , TREE[root*2]
        L = f(root.left)
        R = f(root.right)
        result = calc(L, R, )
        return result
"""

"""
반복문 사용해서 위치 계산해서

def f(root):
     if base : # 왼쪽 오른 쪽 없는 경우
            return root의 값
    
    if root 왼쪽에 트리가 있으면 # TREE[root][0]: , TREE[root*2]
         = f(root.left)
        root 위치에 += f(root.right)
        result = calc(L, R, )
        return result
"""

