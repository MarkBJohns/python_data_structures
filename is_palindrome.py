import re

def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    phrase = re.sub(r'\W+', '', phrase.lower())
    return phrase == phrase[::-1]

print(f'is_palendrome("A man, a plan, a canal, Panama!") = {is_palindrome("A man, a plan a canal, Panama!")}')

print(f'is_palindrome("aibohphobia") = {is_palindrome("aibohphobia")}')

print(f'is_palindrome("Not a palindrome") = {is_palindrome("Not a palindrome")}')