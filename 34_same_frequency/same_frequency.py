def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    count1 = {}
    count2 = {}
    a = num1
    b = num2

    for x in a:
        count1[x] = count1[x].get(x, 0) + 1
        return count1
    for x in b:
        count2[x] = count2[x].get(x, 0) + 1
        return count2
    return count1 == count2

print(same_frequency(551122, 221515))