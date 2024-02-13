def truncate(phrase, n):
    """Return truncated-at-n-chars version of  phrase.
    
    If the phrase is longer than, or the same size as, n make sure it ends with '...' and is no
    longer than n.
    
        >>> truncate("Hello World", 6)
        'Hel...'
        
        >>> truncate("Problem solving is the best!", 10)
        'Problem...'
        
        >>> truncate("Yo", 100)
        'Yo'
        
    The smallest legal value of n is 3; if less, return a message:
    
        >>> truncate('Cool', 1)
        'Truncation must be at least 3 characters.'

        >>> truncate("Woah", 4)
        'W...'

        >>> truncate("Woah", 3)
        '...'
    """
    if n < 3:
        return 'Truncation must be at least 3 characters'
    else:
        short_phrase = phrase[:n-3]
        return f'{short_phrase}...'
    
print("To whom it may concern,", 17)
print(truncate("To whom it may concern", 17))

print("I was born at a very young age,", 20)
print(truncate("I was born at a very young age", 20))

print("Too short,", 2)
print(truncate("Too short", 2))

print("Just right,", 3)
print(truncate("Just right", 3))