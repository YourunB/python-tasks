def max_repetitions():
    s = input()
    if not s:
        print(0)
        return 0
    
    max_count = 1
    current_count = 1 
    
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            current_count += 1
        else:
            max_count = max(max_count, current_count)
            current_count = 1
    
    max_count = max(max_count, current_count)
    
    print(max_count)
    return max_count

max_repetitions()