import string
from collections import Counter

def remove_punctuation(word):
    return word.translate(str.maketrans('', '', string.punctuation))

def has_unique_chars(word):
    return len(set(word)) >= 4

def main():
    text = input().strip().lower()
    words = text.split()
    cleaned_words = [remove_punctuation(word) for word in words]
    word_count = Counter(cleaned_words)
    
    filtered_words = [word for word, count in word_count.items()
        if len(word) >= 5 and has_unique_chars(word) and count > 2]
    
    filtered_words.sort()
    
    for word in filtered_words:
        print(word)

if __name__ == '__main__':
    main()
