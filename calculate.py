def calculate(operation, a, b, make_int=False, message='The result is'):
    """Perform operation on a + b, ()possibly truncating) & returning w/msg.

    - operation: 'add', 'subtract', 'multiply', or 'divide'
    - a and b: values to operate on
    - make_int: (optional, defaults to False) if True, truncates to integer
    - message: (optional) message to use (if not provided, use 'The result is')

    Performs math operation (truncating if make_int), then returns as
    "[message] [result]"

        >>> calculate('add', 2.5, 4)
        'The result is 6.5'

        >>> calculate('subtract', 4, 1.5, make_int=True)
        'The result is 2'

        >>> calculate('multiply', 1.5, 2)
        'The result is 3.0'

        >>> calculate('divide', 10, 4, message='I got')
        'I got 2.5'

    If a valid operation isn't provided, return None.

        >>> calculate('foo', 2, 3)
        
    """
    operations = {
        'add': lambda: a+b,
        'subtract': lambda: a-b,
        'multiply': lambda: a*b,
        'divide': lambda: a/b
    }
    if operation not in operations:
        return None
    result = operations[operation]()
    if make_int:
        result = int(result)

    return f'{message} {result}'

print(calculate('add', 2.4, 2.6))
print(calculate('add', 2.4, 2.6, make_int=True))
print(calculate('add', 2.7, 2.4, message="The sum is"))
print(calculate('add', 2.7, 2.4, make_int=True, message="The sum is"))

print(calculate('subtract', 10, 2.7))
print(calculate('subtract', 11, 3.8, make_int=True))
print(calculate('subtract',9, 22, message="The difference is"))
print(calculate('subtract', 8, 2.1, make_int=True, message="The difference is"))

print(calculate('multiply', 2.1, 7))
print(calculate('multiply', 6.2, 7.1, make_int=True))
print(calculate('multiply', 8.4, 3.2, message="The product is"))
print(calculate('multiply', 7.1, 9.2, make_int=True, message="The product is"))

print(calculate('divide', 12, 3.2))
print(calculate('divide', 13.2, 1, make_int=True))
print(calculate('divide', 5, 7.4, message="The quotient is"))
print(calculate('divide', 11.2, 3, make_int=True, message="The quotient is"))