def histogram(s):
    """ returns a dictionary of the numbers of each character
    s: a string or list
    """
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

print(histogram('kazmator'))