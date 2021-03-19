'''
2
5 3
2 5 3
7 2
4 6
'''

T = int(input())
for tc in range(1, T+1):
    all_stu, sumbit_stu = map(int, input().split())
    submit_sut_num = list(map(int, input().split()))
    arr = [0] * (all_stu+1)
    for i in submit_sut_num:
        arr[i] += 1
    non = []
    for i in range(1, len(arr)):
        if arr[i] == 0:
            non.append(str(i))

    answer = ' '.join(non)
    print('#{} {}'.format(tc, answer))