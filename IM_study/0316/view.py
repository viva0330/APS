import sys
sys.stdin = open('view_input.txt')

T = 10
for tc in range(1, T+1):
    test_len = int(input())
    test_case = list(map(int, input().split()))
    result = 0
    for i in range(2, test_len-2):
        m = max(test_case[i-2], test_case[i-1], test_case[i+1], test_case[i+2])
        if test_case[i] - m > 0:
            result += test_case[i]-m
    print('#{} {}'.format(tc, result))
