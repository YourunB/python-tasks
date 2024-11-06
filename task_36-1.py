str = input()

str_lower = str.lower()
str_result = ''
count = 0

for l in str_lower:
    if l.isalpha() or l == ' ' or l.isdigit():
        str_result += l
    else: count += 1

print(count)
print(str_result)