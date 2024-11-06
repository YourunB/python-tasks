n = int(input())
arr_max = []

for _ in range(n):
    line = input().split()
    try:
        line = [int(x) for x in line if x.strip() != '']
        if line:
            arr_max.append(max(line))
    except ValueError:
        continue

arr_sort = sorted(set(arr_max), reverse=True)

result = ';'.join(str(x) for x in arr_sort)
print(result)
