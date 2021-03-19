def max_chk(lst):
    max_value = 0
    max_pos = 0

    for i in range(10):
        if max_value <= lst[i]:
            max_value = lst[i]
            max_pos = i

    return max_pos, max_value

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ai = input()
    arr = [0] * 10

    for i in range(N):
        arr[int(ai[i])] += 1

    print('#{} {} {}'.format(tc, max_chk(arr)[0], max_chk(arr)[1]))