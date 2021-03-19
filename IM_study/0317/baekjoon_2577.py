A = int(input())
B = int(input())
C = int(input())

ABC = str(A * B * C)
arr = [0] * 10

for number in ABC:
    arr[int(number)] += 1

for num in arr:
    print(num)