def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    words = phrase.split()
    words = [word[0].upper() + word[1:].lower() for word in words]
    return ' '.join(words)

print(titleize('THIS string IS A mesS'))