"""
 0~9까지 숫자카드 4세트를 섞은 후 6개의 카드를 골랐을 때 연속적인 숫자가 3개 이상이면 run
 같은 숫자가 3개 이상이면 triplet
 먼저 run 이나 트리플릿이 되는 사람이 승자!
플레이어 1이 이미 트리플릿을 받으면 이미 win
chk 를 만들어서 triplet이나 run을 체크하는 함수가 필요.
베이비진의 완전검색은 순열을 이용.

각 현재기준으로(단계별로) cnt배열을 만든다
최선의 방법을 찾는다
-현재기준으로 run, triplet이 발견되는지 확인(끝)
-현재 기준을 변경
"""
def chk(i_arr):
    cnt = []
    for data in i_arr:
        cnt[data] += 1

    # 트리플릿
    for i in range(10):
        if cnt[i] == 3:
            return True
    # 런
    for i in range(8):
        if cnt[i] > 0 and cnt[i+1] > 0 and cnt[i+2] >0 :
            return True

    return False



T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    lst = []
    # 3개짜리로 체크하는 함수
    print('#{} '.format(tc))
    for i in range(3, 7):
        if chk(lst[0:i*2:2]):
            print('1')
            break
        if chk(lst[0:i*2+1:2]):
            print('2')
            break
    else:
        print('0')

    """
    for i in range(len(arr)):
        if len(a_list) !=0 and len(b_list)!=0:
            chk(a_list, b_list)
        if i % 2:
            a_list.append(arr[i])
        else:
            b_list.append(arr[i])
    print(a_list)
    print(b_list)
    """

