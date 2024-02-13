def friend_date(a, b):
    """Given two friends, do they have any hobbies in common?

    - a: friend #1, a tuple of (name, age, list-of-hobbies)
    - b: same, for friend #2

    Returns True if they have any hobbies in common, False is not.

        >>> elmo = ('Elmo', 5, ['hugging', 'being nice'])
        >>> sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
        >>> gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])

        >>> friend_date(elmo, sauron)
        False

        >>> friend_date(sauron, gandalf)
        True
    """
    a_hobbies = a[2]
    b_hobbies = b[2]

    for hobby in a_hobbies:
        if hobby in b_hobbies:
            return True
        
    return False

bob = ('Robert', 21, ['eating', 'video games', 'sleeping'])
print(f'bob = {bob}')
pete = ('Peter', 25, ['video games', 'coding', 'card games'])
print(f'pete = {pete}')
joey = ('Joseph', 23, ['bodybuilding', 'eating', 'rock climbing'])
print(f'joey = {joey}')

print(f'friend_date(bob, pete) = {friend_date(bob, pete)}')

print(f'friend_date(bob, joey) = {friend_date(bob, joey)}')

print(f'friend_date(pete, joey) = {friend_date(pete, joey)}')