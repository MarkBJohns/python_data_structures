def intersection(l1, l2):
    """Return intersection of two lists as a new list::
    
        >>> intersection([1, 2, 3], [2, 3, 4])
        [2, 3]
        
        >>> intersection([1, 2, 3], [1, 2, 3, 4])
        [1, 2, 3]
        
        >>> intersection([1, 2, 3], [3, 4])
        [3]
        
        >>> intersection([1, 2, 3], [4, 5, 6])
        []
    """
    return [_ for _ in l1 if _ in l2]

print(f'intersection([1, 2, 3 ,4], [3, 4, 5, 6])')
print(intersection([1, 2, 3, 4], [3, 4, 5, 6]))

print(f'intersection([1, 2, 3], [4, 5, 6])')
print(intersection([1, 2, 3], [4, 5, 6]))

print(f'intersection([3, 2, 1] [1, 2, 3])')
print(intersection([3, 2, 1], [1, 2, 3]))