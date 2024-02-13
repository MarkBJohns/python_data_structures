def repeat(phrase, num):
    """Return phrase, repeated num times.

        >>> repeat('*', 3)
        '***'

        >>> repeat('abc', 2)
        'abcabc'

        >>> repeat('abc', 0)
        ''

    Ignore illegal values of num and return None:

        >>> repeat('abc', -1) is None
        True

        >>> repeat('abc', 'nope') is None
        True
    """
    if not isinstance(num, (int, float)) or num < 0:
        return None
    return phrase * num

print('repeat("haha", 3)')
print(repeat('haha', 3))
print(f'is None = {repeat("haha",3) is None}')

print('repeat("empty", 0)')
print(repeat('empty', 0))
print(f'is None = {repeat("empty",0) is None}')

print('repeat("false", False)')
print(repeat('false', False))
print(f'is None = {repeat("false", False) is None}')

print('repeat("negative", -1)')
print(repeat('negative', -1))
print(f'is None = {repeat("negative", -1) is None}')

print('repeat("string", "STRING!")')
print(repeat('string', 'STRING!'))
print(f'is None = {repeat("string", "STRING!") is None}')