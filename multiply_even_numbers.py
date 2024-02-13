def multiply_even_numbers(nums):
    """Multiply the even numbers.
    
        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48
        
        >>> multiply_even_numbers([3, 4, 5])
        4
        
    If there are no even numbers, return 1.
    
        >>> multiply_even_numbers([1, 3, 5])
        1
    """
    result = 1
    even_list = [num for num in nums if num % 2 == 0]
    if even_list == []:
        return result
    for num in even_list:
        result *= num
    return result

print(f'multiply_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) =')
print(multiply_even_numbers([1,2,3,4,5,6,7,8,9,10]))

print(f'multiply_even_numbers([2, 4, 7, 9, 11])')
print(multiply_even_numbers([2, 4, 7, 9 ,11]))

print(f'multiply_even_numbers([1, 3, 5, 7, 9])')
print(multiply_even_numbers([1, 3, 5, 7, 9]))