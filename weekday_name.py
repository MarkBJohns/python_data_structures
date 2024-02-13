def weekday_name(day_of_week):
    """Return name of weekday.
    
        >>> weekday_name(1)
        'Sunday'
        
        >>> weekday_name(7)
        'Saturday'
        
    For days not between 1 and 7, return None
    
        >>> weekday_name(9)
        >>> weekday_name(0)
    """
    weekdays = [
        None, 'Sunday', 'Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday', 'Saturday']
    try:
        return weekdays[day_of_week]
    except IndexError:
        return None
    
print(f'weekday_name(0) = {weekday_name(0)}')

print(f'weekday_name(1) = {weekday_name(1)}')

print(f'weekday_name(2) = {weekday_name(2)}')

print(f'weekday_name(3) = {weekday_name(3)}')

print(f'weekday_name(4) = {weekday_name(4)}')

print(f'weekday_name(5) = {weekday_name(5)}')

print(f'weekday_name(6) = {weekday_name(6)}')

print(f'weekday_name(7) = {weekday_name(7)}')

print(f'weekday_name(8) = {weekday_name(8)}')

print(f'weekday_name(9) = {weekday_name(9)}')

print(f'weekday_name(10) = {weekday_name(10)}')
