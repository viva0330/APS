words = input()
words_dict = {}
for word in words:
        if not words_dict[word] :
            words_dict[word] = 1
print(words_dict)