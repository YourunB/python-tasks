def str_input(str = ''):
    str_mod = ''
    res = ''

    if len(str) > 0:
        if str[0] == '!':
            str_mod = str.upper()
        else:
            str_mod = str.lower()

    for char in str_mod:
        if char not in "!@#%":
            res += char
    
    return res

while True:
    line = input()
    
    if line == '':
        break

    print(str_input(line))