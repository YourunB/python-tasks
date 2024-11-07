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