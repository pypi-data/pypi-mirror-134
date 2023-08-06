def get_nth_harmonic(n):
    '''
    
    Returns the sum of the reciprocals of the first n natural numbers
    
    '''
    _harm_list = [1/i for i in range(1,n+1)]
    _harm = sum(_harm_list)
    return round(_harm, 2)
