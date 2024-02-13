def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    return [i for i in lst if i]

print(f'compact([False, [], "hello", None, "world", 12])')
print(compact([False, [], "hello", None, "world", 12]))

print(f'compact([0, True, {{}}, 24])')
print(compact([0, True, {}, 24]))