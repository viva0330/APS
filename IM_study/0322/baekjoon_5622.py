words = input()
change_word = ''
for word in words:
    if word == 'A' or 'B' or 'C':
        word = '2'
    elif word == 'D' or 'E' or 'F':
        word = '3'
    elif word == 'G' or 'H' or 'I':
        word = '4'
    elif word == 'J' or 'K' or 'L':
        word = '5'
    elif word == 'M' or 'N' or '0':
        word = '6'
    elif word == 'P' or 'Q' or 'R' or 'S':
        word = '7'
    elif word == 'T' or 'U' or 'V':
        word = '8'
    elif word == 'W' or 'X' or 'Y' or 'Z':
        word = '9'
    change_word += word
print(change_word)