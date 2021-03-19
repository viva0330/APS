C = int(input())
for tc in range(1, C+1):
    s = list(map(int, input().split()))

    students = s[0]
    student_scores = s[1:]
    student_avg = sum(student_scores)//students

    over_avg = 0
    for student_score in student_scores:
        if student_score > student_avg:
            over_avg += 1
    answer = over_avg/students*100
    print(format(answer, '.3f'), end="")
    print('%')