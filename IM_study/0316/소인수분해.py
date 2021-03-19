T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [0] * 12
    num = [2, 3, 5, 7, 11]
    print('#{} '.format(tc), end="")
    while N > 2:
        if N % 2 == 0:
            arr[2] += 1
            N //= 2
        elif N % 3 == 0:
            arr[3] += 1
            N //= 3
        elif N % 5 == 0:
            arr[5] += 1
            N //= 5
        elif N % 7 == 0:
            arr[7] += 1
            N //= 7
        elif N % 11 == 0:
            arr[11] += 1
            N //= 11
        else:
            continue
    for i in range(len(arr)+1):
        if i in num:
            print(arr[i], end=" ")
    print()
