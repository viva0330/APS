import sys
sys.stdin = open('flatten_input.txt')

T = 10
for tc in range(1, T+1):
    dump_number = int(input())
    box_height = list(map(int, input().split()))
    while dump_number != 0 :
        box_height[box_height.index(max(box_height))] -= 1
        box_height[box_height.index(min(box_height))] += 1
        dump_number -= 1
    max_height = max(box_height)
    min_height = min(box_height)
    print('#{} {}'.format(tc, max_height-min_height))