line = 'Hello World'
words = line.split()
rev_words = []
for word in words:
    rev_words.append(word[::-1])
print(' '.join(rev_words))