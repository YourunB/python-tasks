#solution 1
str = input().lower()

nums = []
chars = []

for char in str:
    if char.isdigit():
        nums.append(char)
    else: 
        if char != ' ':
            chars.append(char)

nums = sorted(list(set(nums)))
chars = sorted(list(set(chars)))

res = nums + chars

print(' '.join(res))

#solution 2
input_string = input().strip()
cleaned_string = input_string.replace(' ', '').lower()
unique_chars = set(cleaned_string)
sorted_chars = sorted(unique_chars)
print(" ".join(sorted_chars))