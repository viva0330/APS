T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ai = list(map(int, input().split()))

    for i in ai:
        if i <= i+1:
            max_value = i+1
        max_value = i
