T = int(input())
for tc in range(1, T+1):
    val = float(input())
    a = 0.5
    cnt = 0
    result = []
    while val > 0 and cnt < 13:
        if val >= a:
            result.append("1")
            # print("1")
        else:
            result.append("0")
            # print('0')
        a = a * 0.5
        cnt += 1
    print('#{}'.format(tc))
    if cnt == 13:
        print('overflow')
    else:
        print(result)