import sys
sys.stdin = open('단조증가_input.txt')


def chk(num):
    # 단조만 체크
    temp = num % 10 # 나머지
    num //= 10 # 몫
    while num:
        if num % 10 > temp :
            return False
        temp = num % 10
        num = num // 10
    return True


def chk2(num):
    a = str(num)
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            return False
    return True


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    # 조합 만들고, 그 후에 단조체크!
    ans = -1
    for i in range(N - 1):
        for j in range(i + 1, N):
            num = arr[i] * arr[j]
            if chk2(num):
                if ans < num : ans = num
    print('#{} {}'.format(tc, ans))