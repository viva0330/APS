words = input().upper()
max_count = 0 #
chk = {}
answer = ''
for word in words:
    # count = chk.get(key값, default값) + 1
    count = chk.get(word, 0) + 1
    # 세어진 word값을 가진 dict의 value값 == count
    chk[word] = count
    if max_count < count:
        max_count = count
        answer = word
    elif max_count == count:
        answer = "?"

print(answer)