def to_string(*data, sep=' ', end='\n'):
    return sep.join([str(s) for s in data]) + end
