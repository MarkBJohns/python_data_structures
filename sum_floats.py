def sum_floats(nums):
    """Return sum of floating point numbers in nums.
    
        >>> sum_floats([1.5, 2.4, 'awesome', [], 1])
        3.9
        
        >>> sum_floats([1, 2, 3])
        0
    """
    result = 0
    for num in nums:
        if isinstance(num, float):
            result += num

    return result

print('sum_floats([1, 2, 4.4, True, "hello world"])')
print(sum_floats([1, 2, 4.4, True, "hello world"]))

print('sum_floats([1.2, 5, 3.4, False])')
print(sum_floats([1.2, 5, 3.4, False]))
