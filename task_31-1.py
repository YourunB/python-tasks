def middle(sequence):
    nums = list(map(int, sequence.split()))

    if nums:
        return round(sum(nums) / len(nums), 2)
    else:
        return 0

while True:
    line = input()

    if line == '':
        break

    print(middle(line))