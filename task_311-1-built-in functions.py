from typing import List, Dict

def make_most_common_keys(d: Dict[int, int]) -> List[int]:
    sorted_keys = sorted(d, key=d.get, reverse=True)
    return sorted_keys

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)