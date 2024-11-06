str = input()

words = str.split(' ')

print(round(sum(len(word) for word in words) / len(words), 2))