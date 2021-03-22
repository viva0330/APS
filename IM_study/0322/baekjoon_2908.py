samgun_list = input().split()
max_number = 0
for i in range(len(samgun_list)):
    samgun_number = ''
    for j in range(len(samgun_list[i])-1, -1, -1):
        samgun_number += samgun_list[i][j]
    samgun_number = int(samgun_number)
    if max_number < samgun_number:
        max_number = samgun_number
print(max_number)