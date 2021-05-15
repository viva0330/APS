def binary_search(l, r, key):
    global lst
    d = -1  # left = 0 right = 1
    if l > r:
        return 0

    m = (l+r)//2

    if lst[m] == key:
        return 1

    elif lst[m] < key:
        if d == 1:
            return 0
        d = 1
        t = binary_search(m+1, r, key)
        return t

    else:
        if d == 0:
            return 0
        d = 0
        t = binary_search(l, m-1, key)
        return t


T = int(input())
for tc in range(1, T+1):

    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    binary_search(lst[0], lst[-1], )