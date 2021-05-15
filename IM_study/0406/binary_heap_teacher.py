def insertHeap(data):
    # 맨 마지막노드의 위치
    pos = len(HEAP)
    HEAP.append(data)
    # 만약에 pos가 루트노드이고, 비교관계가 아래처럼 된다면..
    while pos > 1 and HEAP[pos] < HEAP[pos // 2]:
        # 두 값을 바꿔주고
        HEAP[pos], HEAP[pos // 2] = HEAP[pos // 2], HEAP[pos]
        # 부모 노드로 pos 를 변경
        pos //= 2
# return 값이 없어도 되는 이유 : list는 주소참조이기 때문에,,!

# 마지막 노드의 조상 노드에 저장된 정수의 합
def sum_node():
    # HEAP의 마지막노드 -1 의 부모노드 ==> 인덱스는 0부터 시작하기 때문,,,,,,,,,, (이걸 몰랏네,,,
    pos = (len(HEAP)-1) // 2
    sum_value = 0
    while pos >= 1:
        sum_value += HEAP[pos]
        pos = pos // 2
    return sum_value


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    # 노드가 1부터 시작하게 할거니까...
    HEAP = [0]
    # 반복문을 돌려서, lst 값을 data에 data에 넣어주고
    # -> reason : lst에는 data값 하나씩만 들어가기 때문에,,!
    # 반복문이 끝나면 sum_node를 불러오면 댄다고요,,?

    for i in range(len(lst)):
        insertHeap(lst[i])

    print('#{} {}'.format(tc, sum_node()))