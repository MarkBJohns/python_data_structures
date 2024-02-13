def last_element(lst):
    """Return last item in list (None if list is empty.
    
        >>> last_element([1, 2, 3])
        3
        
        >>> last_element([]) is None
        True
    """
    try:
        return lst[-1]
    except IndexError:
        return None
    
print(f'last_element([1, 2, 3]) = {last_element([1, 2, 3])}')

print(f'last_element(["The", "final", "item"]) = {last_element(["The", "final", "item"])}')

print(f'last_element([]) = {last_element([])}')