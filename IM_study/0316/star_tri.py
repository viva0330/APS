T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    print('#{} '.format(tc))
    mid = N // 2

    if M == 1:
        for i in range(N):
            if i < mid:
                for j in range(i+1):
                    print('*', end="")
            else:
                for j in range(N-i):
                    print('*', end="")
            print()
    # elif M == 2:
    #
    #

    elif M == 3:
        # 공백 찍는 법..!
        for i in range(N):
            if i < mid:
                # 공백 찍고
                for j in range(i):
                    print(' ', end="")
        #       # 별찍기
                for j in range((mid-i)*2+1):
                    print('*',end="")
            else:
                for j in range(N-i-1):
                    print(' ', end="")
                      # 별찍기
                for j in range((i-mid)*2+1):
                    print('*', end="")
            print()
    # else:
