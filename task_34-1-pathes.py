from itertools import zip_longest
from typing import List, Tuple

def fill_missing_values(values_list_1: List[int], values_list_2: List[int]) -> List[Tuple[int, int]]:
    return [(a if a is not None else 1, b if b is not None else 1) for a, b in zip_longest(values_list_1, values_list_2)]

result = fill_missing_values([1, 2, 3], [2, 3, 4, 5])

print(result)
