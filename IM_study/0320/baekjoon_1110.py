N = int(input())
# N의 사이클 길이를 구하는 프로그램,
count = 0
change_N = N
new_number = 0
if N == 0:
    count = 1
else:
    while new_number != N:
            right_number = change_N % 10
            left_number = change_N // 10
            new_number = right_number*10 + (left_number+right_number)%10
            change_N = new_number
            count += 1
print(count)
