T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    carrot_size_list = list(map(int, input().split()))

    count = 1
    max_count = 1

    for i in range(1, len(carrot_size_list)):
        if carrot_size_list[i - 1] < carrot_size_list[i]:
            count += 1
            max_count = max(count, max_count)
        else:
            count = 1

    print("#{} {}".format(tc, max_count))