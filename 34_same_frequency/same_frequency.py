def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    num1_str = str(num1)
    num2_str = str(num2)
    
    digits = {1,2,3,4,5,6,7,8,9}
    
    freq1 = {}
    freq2 = {}
    
    for digit in num1_str:
        freq1[digit] = freq1.get(digit, 0) + 1
    for digit in num2_str:
        freq2[digit] = freq2.get(digit, 0) + 1
    
    if len(freq1) != len(freq2):
        return False
    for key in freq1:
        if key not in freq2 or freq1[key] != freq2[key]:
            return False

    return True