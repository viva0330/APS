"""
횟수가 정해
한번 바꾸고

"""
for i in range(N-1):
    for j in range(i+1, N):
        # 1 . 교환
        a = A[i], A[j] = A[j], A[i]
        # 2. 숫자로 만들어서 중복이 없도록 넣기(예- set 사용)

# 얘를 기준으로 두 번째 바꾼다.
N = len(t)
for i in range(N-1):
    for j in range(i+1, N):
        # 1 . 교환
        a = A[i], A[j] = A[j], A[i]
# 얘를 N번..! 복사가 이루어지면 좋지 않으니까 저장공간을 어떻게하면 효율적으로 만들 수 있을지 고민.

# 2.
# 이게 기본구조이지만 이렇게 하면 시간초과가 많이 남..!
# 가지치기..! 필요!
# 최대 가능성 있는 값
def solve(k):
    # 두개씩 바꾸는 ...!
    # num에 a에 있는 값을 숫자로 만들어서
    # 만약 num이 가능성과 같아지면..!
    # ex) 가능성 321 가능성 88832
    """
    if num = possible and 교환할 남은 횟수가 짝수이면 :
        maxVal = possible
        return
    """
    if k == K:
        ???
        return
    for i in range(N-1):
        for j in range(i+1, N):
            A[i], A[j] = A[j], A[i]
            solve(k+1)
            A[i], A[j] = A[j], A[i]

T = int(input())
for ~
    possible = 정렬해서 숫자로 만들어 넣으면 됩니다..!
    # 교환 횟수가 K가 맞을까?
    # 보내기전에 K의 값을 조정해주어야함
    # 만약 4개밖에 없는데 100번 교환.
    K = 조정
    solve(K)