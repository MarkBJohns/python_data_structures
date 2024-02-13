def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?
    
        >>> single_letter_count('Hello World', 'h')
        1
        
        >>> single_letter_count('Hello World', 'z')
        0
        
        >>> single_letter_count("Hello World", 'l')
        3
    """
    return word.lower().count(letter.lower())

print(f'single_letter_count("octopus", "o") = {single_letter_count("octopus", "o")}')

print(f'single_letter_count("She sells seashells by the seashore", "s") = {single_letter_count("She sells seashells by the seashore", "s")}')