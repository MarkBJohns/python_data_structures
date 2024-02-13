def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    first_letter = phrase[0].upper()
    phrase = phrase[1:]
    return f'{first_letter}{phrase}'

print(capitalize('hello world'))