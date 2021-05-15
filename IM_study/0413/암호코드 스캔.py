import sys
sys.stdin = open('암호코드.txt')


def findP():
    # 들어온 문자열 봐서 리턴..!
    # 결과물로 n_list = [7, 5, 7, 5, 5, 0, 2, 7] 나오는 함수 생성,,!


T = int(input())
# 입력
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 얘 입력을 왜 이렇게 못 받지,,?
    arr = [list(map(int, input().split())) for _ in range(N)]

# 코드를 찾는다.
# 2-1 시작 코드를 찾아서(56개의 데이터) 힌트 : 모든 코드는 끝이 1로 끝난다
for row in range(row의 갯수):
    for col in range(마지막, -1, -1):
        arr[row][col] == '1'
        y_pos = row
        x_pos = col
        break
    # 여기로부터 시작점은 전체 사이즈로부터 56개 그러니까
    x_pos = x_pos - 56 + 1
    # 2-2 7개씩 잘라서 패턴에서 찾는다.
    for i in range(7):
        nlist.append(findP(arr[x_pos:x_pos+7]))
        # findP는 문자열가져다가 ..


# 검증
    if (nlist[0] + nlist[2] + nlist[4]+ nlist[6]) * 3 + nlist[1]+ nlist[3]+ nlist[5]+ nlist[7] % 10:
        nlist의 합
    else:
        print(0)