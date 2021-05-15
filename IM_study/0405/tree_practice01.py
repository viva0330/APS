# 다음 이진 트리 표현에 대하여 전위 순회하여 정점의 번호를 출력하시오.
# 정점의 개수 13
# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13

data = [[], [2, 3], [4, 0], [5, 6], [7, 0], [8, 9], [10, 11], [12, 0], [], [], [], [0, 13]]

# 일차원 배열
# data = [0, 1, 2, 3, 4, 0, 5, 6, 7, 0, 0, 0, 8, 9, 10, 11, 12, 0, 0, 0, 13]
lst = list(map(int, input().split()))
for i in range(0, len(data), 2):
    p = lst[i]
    c = list[i+1]
    if data[p][0] == 0: # 왼쪽 자식 노드가 없으면
        data[p][0] == c
    else:
        data[p][1] == c

'''
lst = list(map(int, input().split()))
for i in range(0, len(lst), 2):
    # for문 돌려도 되고 index찾는 함수 사용해도 됨
    p = lst[i]의 index를 찾아야함! data와 인덱스의 차이!
    c = list[i+1]
    if 왼쪽 자식 노드가 없으면...:
        data[p*2] == c
    else:
        data[p*2+1] = c
'''