start, end, step = map(int, input().split())
seq = range(start, end, step)
for i in map(lambda x: x**2 if x % 2 != 0 else -x, seq):
    print(i)
