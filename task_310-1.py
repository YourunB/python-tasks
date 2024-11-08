str = input().lower()
arr = str.split()

word_count = {}

for word in arr:
    word_count[word] = 0

for word in arr:
    if word in word_count:
        word_count[word] += 1

max_key = max(word_count, key=word_count.get)
print(max_key, word_count[max_key]) 