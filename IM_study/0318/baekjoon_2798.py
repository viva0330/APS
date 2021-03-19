N, M = map(int, input().split())
arr = list(map(int, input().split()))

max_value = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sum_value = arr[i] + arr[j] + arr[k]
            if sum_value <= M:
                max_value = max(sum_value, max_value)
print(max_value)