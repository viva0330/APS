N, X = map(int, input().split())
number_arr = list(map(int, input().split()))
for number in number_arr:
    if number < X:
        print(number, end=" ")