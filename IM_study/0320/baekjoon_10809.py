S = input()
# alphabet = {
#     'a' : -1, 'b' : -1, 'c' : -1, 'd' : -1, 'e' : -1, 'f' : -1, 'g' : -1, 'h' : -1, 'i' : -1, 'j' : -1, 'k' : -1, 'l' : -1,'m' : -1, 'n' : -1,'o' : -1,'p' : -1,
#     'q' : -1, 'r' : -1, 's' : -1, 't' : -1, 'u' : -1, 'v' : -1, 'w' : -1, 'x' : -1, 'y' : -1, 'z' : -1,
# }
#
# for i in S:
#     if i in alphabet:
#         alphabet[i] = S.find(i)
#
# print(*alphabet.values())

alphabet = [-1 for _ in range(26)]

for i in range(len(S)):
    index = ord(S[i]) - ord('a')
    if alphabet[index] == -1:
        alphabet[index] = i

print(*alphabet)


alphabet = {
    'a' : -1, 'b' : -1, 'c' : -1, 'd' : -1, 'e' : -1, 'f' : -1, 'g' : -1, 'h' : -1, 'i' : -1, 'j' : -1, 'k' : -1, 'l' : -1,'m' : -1, 'n' : -1,'o' : -1,'p' : -1,
    'q' : -1, 'r' : -1, 's' : -1, 't' : -1, 'u' : -1, 'v' : -1, 'w' : -1, 'x' : -1, 'y' : -1, 'z' : -1,
}

for i in range(len(S)):
    if alphabet[S[i]] == -1:
        alphabet[S[i]] = i

print(*alphabet.values())