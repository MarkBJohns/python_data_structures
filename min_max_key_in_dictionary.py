def min_max_keys(d):
    """Return tuple (min-keys, max-keys) in d.

        >>> min_max_keys({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'})
        (1, 10)

    Works with any kind of key that can be compared, like strings:

        >>> min_max_keys({"apple": "red", "cherry": "red", "berry": "blue"})
        ('apple', 'cherry')
    """
    return (min(d.keys()), max(d.keys()))

print(min_max_keys({'Bulbasaur': 'Grass', 'Charmander': 'Fire', 'Squirtle': 'Water'}))

print(min_max_keys({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'Z': 6}))