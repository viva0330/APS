answer = 0
N = int(input()) # 분해합.

for i in range(0, N+1):
    str_num = str(i)
    temp_num = i
    for s in str_num:
        temp_num += int(s)
    if temp_num == N:
        answer = i
        break
print(answer)