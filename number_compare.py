def number_compare(a, b):
    """Report on whether a>b, b>a, or b==a
    
        >>> number_compare(1, 1)
        'Numbers are equal'
        
        >>> number_compare(-1, 1)
        'Second is greater'
        
        >>> number_compare(1, -2)
        'First is greater'
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return 'Please try again with a number'
    elif a > b:
        return 'First is greater'
    elif a < b:
        return 'Second is greater'
    else:
        return 'Numbers are equal'

print(f'number_compare(5, 10) = {number_compare(5, 10)}')

print(f'number_compare(10, 5) = {number_compare(10, 5)}')

print(f'number_compare(10, 10) = {number_compare(10, 10)}')

print(f'number_compare("hello", "world") = {number_compare("hello", "world")}')

print(f'number_compare("8", "9") = {number_compare("8", "9")}')