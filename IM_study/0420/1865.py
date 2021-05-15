# 공평하게 일을 하나씩 분배 - > 순열
# 직원 N명 해야할 일 N
# 직원이 i-> j번 일을 하면 성공할 확률이 p
# 동철이가 모든 일이 잘 풀리도록 도와
# 직원들에게 해야할 일을 하나씩 배분.
# 실수로 나누기 식이라 최소 구하는 것처럼 가능
# 1에서 곱할수록 값이 작아짐
# 입력 모양도 동일

def bfs(idx, answer=100):
    global max_value
    # 값이 계산한 이전값보다 작다면 리턴
    if answer <= max_value: return
    # 위에서 걸러지므로 여기까지 왔다면 그냥 값을 넣는다.
    if idx >= N:
        max_value = answer
        return
    # 조합을 구해서 bfs하기
    for i in range(N):
        if use_check[i]:
            use_check[i] = False
            # 더하기가 아니라 곱하기 인것,,,!
            bfs(idx + 1, answer * (success_list[idx][i]))
            use_check[i] = True


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    # 람다식을 이용하여 넣을때부터 100으로 나누어 사용
    success_list = [list(map(lambda x: int(x) / 100, input().split())) for _ in range(N)]
    use_check = [True for _ in range(N)]
    max_value = 0
    bfs(0)
    # 6자리수로 출력
    print('#{} {:6f}'.format(t, max_value))