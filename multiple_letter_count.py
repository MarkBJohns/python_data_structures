def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """

    return {char: phrase.count(char) for char in phrase}
    
print(f'multiple_letter_count("The quick brown fox jumps over the lazy dog") = {multiple_letter_count("The quick brown fox jumps over the lazy dog")}')

print(f'multiple_letter_count("Hello World!") = {multiple_letter_count("Hello World!")}')