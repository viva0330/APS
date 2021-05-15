# 00000000111100000011000000111100110000110000111100111100111111001100111
# 2진수 문자열을 받음

"""
arr = 231
t = 2
t = t * 10+3 = 23
t = t * 10+1 = 230+1
    t = 0
    for i in range(len(arr)):
        t= t * 10 + arr[i]

0000001 = > 1 * 2^0
0000010 => 2
0000011 => 3
0000110 => 1*4 + 1*2 + 0
0010001 => 1*16 + 1*1
a1 a2 a3 a4 a5
a1
t = a1
a1 a2
t = t << 1 +a2
"""

# 0010001이면 가능인데
# '0010001'로 들어오면,,!
def prt(arr):
    # lst에 들어있는 데이터가 7개
    t = 0
    for a in range(len(arr)):
        t = t << 1 + int(arr[a])
    print(t, end=' ')


lst = input()

# 7개로 나눠서 ..
for i in range(len(lst)//7):
    prt(lst[i*7:(i+1)*7])

"""
'i' => 1 : int('1')
'0' => 0 : int('0')
s[i] => 0/1 : int(s[i])
1 = > 0 | 1 => 0 + 1 : t
11 - > t << 1 + 1 == t << 1 | 1

"""
"""
10진수ㄱ 정수를 2진수로 출력하는 함수 만들기
a = 10 a=0b1010
입력값 : 1010
        &
        1000 # filter로 쓰고 check는 1000이 나오던지 0000이 나옴
        0100 # filter로 쓰고 0100 이거나 0000 나옴
        0010 # 0010 0000
        0001 # 0001 0000
        오른쪽으로 쉬프트 시키면서 이동
        # 필터값을 고정해놓고 입력값을 바꾸는 경우도
        1010
        10100
        1000
0
&
10000000
"""
"""
def prt(value):
    # filter = 8
    filter = 0b1000
    # 4자리로 했기 때문에 4이고 7자리고 7개를 하라고 했으면 7로 바뀌어야함
    for i in range(4):
        #t = value & filter
        if value & filter  == 0:
            print('0')
        else:
            print('1')
        filter >>= 1
"""

# 10진수 정수를 2진수의 문자열로 변경하는 함수 만들기
def prt(value):
    filter = 0b1000
    a = []
    for i in range(4):
        if value & filter  == 0:
            a.append('0')
        else:
            a.append('1')
        filter >>= 1



# 16진수 문자열을 2진수의 문자열로 만드는 함수
a = '11E'
# a = 0x11E
# a = 1*16^2 + 1 * 16 + 14 =

# d= '1' , 'E'
def chg1(value):
    # '1' => '0001'
    # '2' => '0002'
    # 'A' => 10이니까 '1010'

    filter = 0b1000
    # a = []
    for i in range(4):
        if value & filter == 0:
            ret.append('0')
        else:
            ret.append('1')
        filter >>= 1



def chg(value):
    ret = []
    for d in value:
        if d.isdecimal():
            chg(int(d))
        else:
            chg(ord(d) - ord('A') + 10)

"""
arr = '11E'
arr.replace('1', '0001')

딕셔너리 쓰는 것도 가능!
"""
