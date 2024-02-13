def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    make_dict = lambda num: {int(digit): str(num).count(digit) for digit in str(num)}

    num1 = make_dict(num1)
    num2 = make_dict(num2)

    return num1 == num2

print(same_frequency(1234, 4321))

print(same_frequency(13527, 72135))

print(same_frequency(1234, 5678))