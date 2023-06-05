def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True

        >>> same_frequency(7754212, 5774421)
        False

    """
    dict1 = {}
    dict2 = {}
    string1 = str(num1)
    string2 = str(num2)
    for n1, n2 in zip(string1, string2):
        if(dict1.get(n1) is None):
            dict1[n1] = string1.count(n1)
        if(dict2.get(n2) is None):
            dict2[n2] = string2.count(n2)
    return dict1 == dict2