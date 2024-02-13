import doctest

def partition(lst, fn):
    """Partition lst by predicate.
     
     - lst: list of items
     - fn: function that returns True or False
     
     Returns new list: [a, b], where `a` are items that passed fn test,
     and `b` are items that failed fn test.

        >>> def is_even(num):
        ...     return num % 2 == 0
        
        >>> def is_string(el):
        ...     return isinstance(el, str)
        
        >>> partition([1, 2, 3, 4], is_even)
        [[2, 4], [1, 3]]
        
        >>> partition(["hi", None, 6, "bye"], is_string)
        [['hi', 'bye'], [None, 6]]
    """
    true_list = []
    false_list = []
    for i in lst:
        if fn(i):
            true_list.append(i)
        elif fn(i) == False:
            false_list.append(i)
    return [true_list, false_list]

def is_even(num):
    if num % 2 ==0:
        return True
    return False

def is_string(string):
    if isinstance(string, str):
        return True
    return False

# print(f'partition([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], is_even')
# print(partition([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], is_even))

# print(f'partition(["hello", 1, 2, "world", 3], is_string)')
# print(partition(["hello", 1, 2, "world", 3], is_string))