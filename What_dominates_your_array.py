def dominator(arr):
    n = len(arr)
    frequency = {}
    for num in arr:
        frequency[num] = frequency.get(num, 0) + 1
        if frequency[num] > n / 2:
            return num
    return -1