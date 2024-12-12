from typing import List

def get_indexes(nums1: List[int], nums2: List[int]) -> List[int]:
    indexes = [i for i, (a, b) in enumerate(zip(nums1, nums2)) if a < b]
    return indexes

code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)
