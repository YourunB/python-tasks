def max_product_subsequence(arr, k):
    arr.sort()
    
    if k == len(arr):
        product = 1
        for num in arr:
            product *= num
        return product
    
    positive = [num for num in arr if num > 0]
    negative = [num for num in arr if num < 0]
    
    if len(positive) >= k:
        positive.sort(reverse=True)
        product = 1
        for i in range(k):
            product *= positive[i]
        return product
    
    product = 1
    count = 0
    
    for num in positive:
        product *= num
        count += 1
    
    negative.sort()
    for i in range(k - count):
        product *= negative[i]
    
    return product

n = int(input())
arr = list(map(int, input().split()))
k = int(input())

print(max_product_subsequence(arr, k))
