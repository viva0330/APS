# def f(pos):
#     f(pos//2)
#
T = int(input())

for tc in range(1, T+1):
    N = int(input()) # N개인 서로 다른 자연수
    lst = list(map(int, input().split()))

    # 2차원 배열로 만들어보자!
    # 몇개를 만들어야할지 모르겠어...
    # TREE = [[0, 0] for _ in range(N)]

    # 라이브 강의 확인해보니까 1차원이 낫다는 거 같다

    # 데이터 개수만큼 돌면서..
    HEAP = [0]
    for data in lst:
        # 내가 만들고자 하는 곳에 넣기..!
        # 마지막에 넣은것,,!
        HEAP.append(data)
        # 들어온 데이터가 하나라면 위치겠지만
        # 마지막에 내 부모로 올라가면서 비교해서 올라가야함
        # 포지션을 계속 바꿔가면서 올라가면 됨(상위까지)
        """
        pos =
        while 최상위가 아니면 혹은 부모노드의 값이 데이터보다 작은 동안:
            부모노드의 값과 현재 위치의 값을 교환한다.
            현재위치를 부모노드의 위치로 변경 (pos = pos // 2)

        # 마지막 데이터를 기준으로 위로 올라가면서 합을 구하면 됨
    while
        while 최상위가 아니면 혹은 부모노드의 값이 데이터보다 작은 동안:
            부모노드의값과 현재 위치의 값을 교환한다.
            현재위치를 부모노드의 위치로 변경(pos=pos // 2)
            sum_value += pos의 값
        """
    #     pos = len(HEAP)
    #     while pos > 1 and HEAP[pos] < HEAP[pos // 2]:
    #         HEAP[pos], HEAP[pos // 2] = HEAP[pos // 2], HEAP[pos]
    #         pos //= 2
    # while
    #     while pos > 1 and HEAP[pos] < HEAP[pos // 2]:
    #         HEAP[pos], HEAP[pos // 2] = HEAP[pos // 2], HEAP[pos]
    #         pos //= 2


    print('#{}'.format(tc))


