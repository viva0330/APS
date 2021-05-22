T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input()))

    # 연속한 갯수
    count = 0
    max_count = 0
    for i in range(len(lst)):
        if lst[i] == 1:
            count += 1
        else:
            count = 0
        max_count = max(max_count, count)

    print("#{} {}".format(tc, max_count))