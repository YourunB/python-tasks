def cache_deco(func):
    cache = {}
    def wrapper(x):
        if x not in cache:
            cache[x] = func(x)
        return cache[x]
    return wrapper

def solution(func_map, func_filter, data):
    filtered_data = (x for x in data if func_filter(x))
    mapped_data = (func_map(x) for x in filtered_data)
    for i, value in enumerate(mapped_data):
        if i % 2 == 0:
            yield value

code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)
