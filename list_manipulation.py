def list_manipulation(lst, command, location, value=None):
    """Mutate lst to add/remove from beginning or end.

    - lst: list of values
    - command: command, either "remove" or "add"
    - location: location to remove/add, either "beginning" or "end"
    - value: when adding, value to add

    remove: remove item at beginning or end, and return item removed

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'remove', 'end')
        3

        >>> list_manipulation(lst, 'remove', 'beginning')
        1

        >>> lst
        [2]

    add: add item at beginning/end, and return list

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'add', 'beginning', 20)
        [20, 1, 2, 3]

        >>> list_manipulation(lst, 'add', 'end', 30)
        [20, 1, 2, 3, 30]

        >>> lst
        [20, 1, 2, 3, 30]

    Invalid commands or locations should return None:

        >>> list_manipulation(lst, 'foo', 'end') is None
        True

        >>> list_manipulation(lst, 'add', 'dunno') is None
        True
    """
    if command == 'remove':
        if location == 'end':
            return lst.pop()
        elif location == 'beginning':
            return lst.pop(0)
    elif command == 'add':
        if location == 'end':
            lst.append(value)
            return lst
        elif location == 'beginning':
            lst.insert(0, value)
            return lst
    return None


list_one = [1, 2, 3, 4, 5]

print(f'list_one = {list_one}')

print(f'list_maninupulation(list_one, "remove", "end") = {list_manipulation(list_one, "remove", "end")}')

print(f'list_one = {list_one}')

print(f'list_manipulation(list_one,"add", "beginning", 0) = {list_manipulation(list_one,"add","beginning",0)}')

print(f'list_manipulation(list_one, "add", "end", 5) = {list_manipulation(list_one, "add", "end", 5)}')

print(f'list_manipulation(list_one, "remove", "beginning") = {list_manipulation(list_one, "remove", "beginning")}')

print(f'list_one = {list_one}')

print(f'list_manipulaton(list_one, "add", "gibberish") = {list_manipulation(list_one, "add", "gibberish")}')

print(f'list_manipulation(list_one, "explode", "beginning", 8) = {list_manipulation(list_one, "explode", "beginning", 8)}')