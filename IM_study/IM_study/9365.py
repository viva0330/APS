T = int(input())
for tc in range(1, T+1):
    N = int(input())
    carrot_area = list(map(int, input().split()))

    max_value = 0
    max_index = 0

    for i in range(len(carrot_area)):
        if max_value < carrot_area[i]:
            max_value = carrot_area[i]
            max_index = i + 1

    print("#{} {} {}".format(tc, max_index, max_value))