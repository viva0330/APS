T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    hap = []
    for i in range(N-2+1):
        for j in range(i, i+1):
            hap.append(lst[j] + lst[j+1])
    print('#{} {} {}'.format(tc, max(hap), min(hap)))