# 10개 이하의 테스트 케이스,

def f(b, t):
    # bint = int(b,2)
    bint = 0
    for x in b:
        bint = bint*2 + int(x)
    binary = []
    for i in range(len(b)):
        binary.append(bint ^ (1 << i)) # 2진수의 1비트씩 바꿔서 저장
    for i in range(len(t)):
        num1 = 0
        num2 = 0
        for j in range(len(t)):
            if 1 != j:
                num1 = num1*3 + int(t[j])
                num2 = num2*3 + int(t[j])
            else:
                num1 = num1*3 + (int(t[j])+1)%3 # 0->1 1->2 2->0
                num1 = num1*3 + (int(t[j])+2)%3 # 0->2 1->0 2->1
        if num1 in binary:
            return num1
        if num2 in binary:
            return num2




TC = int(input())
for test_case in range(1, TC+1):
    binary_number = input()
    tri_number = input()

    r = f(binary_number, tri_number)

    print('#{} {}'.format(test_case, r))