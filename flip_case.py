def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    return ''.join([char.swapcase() if char.lower() == to_swap.lower() else char for char in phrase])

print(f'flip_case("She sells seashells by the seashore", "s") = {flip_case("She sells seashells by the seashore", "s")}')

print(f'flip_case("Peter Piper picked a pair of pickled peppers", "P") = {flip_case("Peter Piper picked a pair of pickled peppers", "P")}')
