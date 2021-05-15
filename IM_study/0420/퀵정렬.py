# 전체 리스트가 있으면 전체 리스트에 피봇이라는 걸 하나 잡아서
# 작은 걸 왼, 큰걸 오른쪽,
# 경계지점을 찾을 수 있는 알고리즘

def quick(left, right):
    global lst
    # 경계지점 찾기!
    if left < right:
        pos = partition(lst, left, right)
        # 왼쪽
        quick(left, pos-1)
        # 오른쪽
        quick(pos+1, right)

    # 두 개를 바꾼다.

def partition(l, r):
    global lst
    # pivot 시작점
    pivot = lst[l]
    # 같을 때는 어떻게 할까? 넘어갈까 아니면 그냥 그 지점에서 멈출까?
    i = l
    j = r
    while i < j:
        while i < r and lst[i] <= pivot:
            i += 1
        while j > l and lst[j] >= pivot:
            j += 1
    #   역전 현상 발생 유무?
        if i < j:
            lst[i], lst[j] = lst[j], lst[i]
    # 경계지점 찾았다는 소리.
    lst[l], lst[j] = lst[j], lst[l]
    return j

def partition_l(l, r):
    global lst
    # 피봇보다 작은 값이 들어있는 작은 값
    pivot = lst[r]
    i = l-1
    for j in range(l, r):
        # 작은게 나타나면 i를 증가하고 넣기..!
        if lst[j] < pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    # 다 하고 나면 i는 경계지점에... 피봇이랑 바꿔줘야해용
    lst[i+1], lst[r] = lst[r], lst[i+1]
    return i+1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    quick(lst[:len(lst//2)], lst[len(lst//2):])

    print('#{} {}'.format(tc, lst[N//2]))