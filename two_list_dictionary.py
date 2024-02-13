def two_list_dictionary(keys, values):
    """Given keys and values, make dictionary of those.
    
        >>> two_list_dictionary(['x', 'y', 'z'], [9, 8, 7])
        {'x': 9, 'y': 8, 'z': 7}
        
    If there are fewer values than keys, remaining keys should have value
    of None:
    
        >>> two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])
        {'a': 1, 'b': 2, 'c': 3, 'd': None}
    
    If there are fewer keys, ignore remaining values:

        >>> two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4])
        {'a': 1, 'b': 2, 'c': 3}
   """
    values.extend([None] * (len(keys) - len(values)))

    return dict(zip(keys, values))

pokelist = ['Bulbasaur', 'Charmander', 'Squirtle']
types = ['Grass', 'Fire', 'Water']

print("['Bulbasaur', 'Charmander', 'Squirtle'], ['Grass', 'Fire', 'Water']")
print(two_list_dictionary(pokelist, types))

bending = ['Water', 'Earth', 'Fire', 'Air']
nations = ['Water Tribe', 'Earth Kingdom', 'Fire Nation']

print(f'{bending}, {nations}')
print(two_list_dictionary(bending,nations))

letters = ['a', 'b', 'c']
numbers = [1, 2, 3, 4]

print(f'{letters}, {numbers}')
print(two_list_dictionary(letters, numbers))