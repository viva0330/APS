count, se_day = map(int, input().split())
every_temp = list(map(int, input().split()))

i = 0
tem_sum = sum(every_temp[0:se_day])
max_sum = tem_sum
if se_day == 1:
    print(max(every_temp))
else:
    while True:
        tem_sum -= every_temp[i]
        if i + se_day >= count:
            break;
        tem_sum += every_temp[i+se_day]
        if max_sum < tem_sum:
            max_sum = tem_sum
        i += 1
    print(max_sum)
