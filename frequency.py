def frequency(lst, search_term):
    """Return frequency of term in lst.
    
        >>> frequency([1, 4, 3, 4, 4], 4)
        3
        
        >>> frequency([1, 4, 3], 7)
        0
    """
    return lst.count(search_term)

num_list = [1, 2, 3, 2, 1, 2, 3, 2]

for value in set(num_list):
    print(f'frequency(num_list, {value}) = {frequency(num_list, value)}')

print(f'frequency(num_list, 12) = {frequency(num_list, 12)}')