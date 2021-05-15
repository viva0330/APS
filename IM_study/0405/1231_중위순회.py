import sys
sys.stdin = open("1231_input.txt")

def inorder(i):
    if i <= N:
        inorder(i*2)
        print(tree[i], end='')
        inorder(i*2+1)

for tc in range(1, 11):
    N = int(input())
    tree = [0] * (N+1)

    for i in range(N):
        arr = list(input().split())
        tree[int(arr[0])] = arr[1]

    print("#{}".format(tc))
    inorder(1)
    print()