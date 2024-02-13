def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    counts = {}
    for num in nums:
        if num not in counts:
            counts[num] = 1
        else:
            counts[num] += 1

    mode = max(counts.values())
    for num, count in counts.items():
        if count == mode:
            return num
        
print(f'mode([2, 3, 2, 2, 1, 3]) = {mode([2, 3, 2, 2, 1, 3])}')
print(f'mode([1, 2, 3, 4, 5, 5]) = {mode([1, 2, 3, 4, 5, 5])}')
