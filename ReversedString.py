text = "Hello World"
words = text.split()

phrase = []
for word in words:
    reversed_word = word[::-1]
    phrase.append(reversed_word)
print(phrase)
reversed_phrase = ', '.join(phrase)
print(reversed_phrase)
