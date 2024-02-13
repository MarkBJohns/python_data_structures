def includes(collection, sought, start=None):
    """Is sought in collection, starting at index start?

    Return True/False if sought is in the given collection:
    - lists/strings/sets/tuples: returns True/False if sought present
    - dictionaries: return True/False if *value* of sought in dictionary

    If string/list/tuple and `start` is provided, starts searching only at that
    index. This `start` is ignored for sets/dictionaries, since they aren't
    ordered.

        >>> includes([1, 2, 3], 1)
        True

        >>> includes([1, 2, 3], 1, 2)
        False

        >>> includes("hello", "o")
        True

        >>> includes(('Elmo', 5, 'red'), 'red', 1)
        True

        >>> includes({1, 2, 3}, 1)
        True

        >>> includes({1, 2, 3}, 1, 3)  # "start" ignored for sets!
        True

        >>> includes({"apple": "red", "berry": "blue"}, "blue")
        True
    """
    if isinstance(collection, dict):
        return sought in collection.values()
    elif isinstance(collection, set):
        return sought in collection
    else:
        return sought in collection[start:]
    
print(includes((1,2,3), 3))
print(includes({1: 'hello', 2: 'world'}, 'world'))
print(includes([1, 2, 3, 4, 5, 6, 7], 7))

print(includes((1,2,3), 5))
print(includes({1: 'hello', 2: 'world'}, 'jupiter'))
print(includes([7, 6, 5, 4, 3, 2, 1], 7, start=3))