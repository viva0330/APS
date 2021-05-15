"""
화물이 실려있는 N개의 컨테이너를 M대의 트럭으로 A도시에서 B도시로 운반.
트럭당 한개의 컨테이너 운반. 적재용량 초과 컨테이너 운반 불가.
A->B 최대 M개의 트럭이 편도로 한 번 만 운행한다고 한다.
총 증량이 최대가 되도록 컨테이너를 옮겼다면 옮겨진 화물의 전체 무게가 얼마인지,,?
화물을 싣지 못한 트럭이나 남는화물이 있을 수 있다. 컨테이너를 하나도 옮길 수 없는 경우
0 을 출력한다.

"""
"""
1. 적재 용량이 큰 트럭순으로 배열
2. 무거운 컨테이너 순으로 배열
3. 최선의 방법을 찾ㅇ는다.
    3-1, 현재 기준으로 가장 무거운 컨테이너를 적재용량 큰 것에 넣기.
    3-2 현재 기준을 변경한다.
그리디 알고리즘은 항상 옳은지 검증 후 사용!
    
ex) 1800
800원 거슬러주려고 한다.
500, 100, 50, 100
    3-1 최선의 방법:
    500 => 1
    300원 남음
    300 => 100자리 3개,,?
    4개
만약에 동전이 400원짜리 동전이 있었다고 치자...!
이 경우에는 400원짜리 2개가 제일 적기 때문 ㅇㅇ,,!
"""
T = int(input())
for tc in range(1, T+1):
    # N : 컨테이너 수, M : 트럭 수
    N, M = map(int, input().split())
    Mlist = list(map(int, input().split())) # 컨테이너 정보
    Nlist = list(map(int, input().split())) # 트럭정보
    Mlist.sort(reverse=True)
    Nlist.sort(reverse=True)
    # 누구를 기준으로 할건지
    # 교수님은 트럭을 기준으로 (내가 따로 컨테이너를 기준으로 돌려보자!)
    # 버리는 작업 위해 인덱스 잡아놓기..!
    idx = 0
    total = 0
    for w in Mlist:
        # 다시 돌리는 작업 필요
        while idx < N and Nlist[idx] > w:
            idx += 1

        if idx < N-1:
            total += Nlist[idx]
            idx += 1
        """
        while idx < N:
            if Nlist[idx] > w:
                idx += 1

            else:
                # 싣었다는 소리 위로 올라가는 작업!
                total += Nlist[idx]
                idx += 1
        """

