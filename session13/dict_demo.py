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

# print(histogram('kazmator'))

#EXERCISE 1######################33
def histogram2(word): #Got help from https://github.com/epequeno/ThinkPy-Solutions/blob/master/ch11/11.02.py
    dictionary = dict()
    for character in word:
        dictionary[character] = 1 + dictionary.get(character, 0)
    return dictionary

print(histogram2("Old MACDONALD had a farm E-I-E-I-O And on his farm he had a cow E-I-E-I-O With a moo moo here And a moo moo there Here a moo, there a moo Everywhere a moo moo Old MacDonald had a farm E-I-E-I-O"))

def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError()


h = histogram('Massachusetts')
key = reverse_lookup(h, 2)
# print(key)

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

hist = histogram('parrot')
# print(hist)

inverse = invert_dict(hist)
# print(inverse)

t = [1, 2, 3]
d = dict()
d[t] = 'oops'

known = {0:0, 1:1}

def fibonacci(n):
    if n in known:
        return known[n]

    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res

# for i in range(10):
#     print(fibonacci(i), end=", ")

#EXERCISE 2###########################################
def fib(n):
    """
    an intuitive version of fibonacci
    """
    global number_fib_calls
    number_fib_calls += 1
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n - 1) + fib(n - 2)


known = {1: 1, 2: 2}


def fib_efficient(n):
    """
    a "memori version of fibonacci
    """
    global number_fib_calls
    number_fib_calls += 1
    if n in known:
        return known[n]
    else:
        ans = fib_efficient(n - 1) + fib_efficient(n - 2)
        known[n] = ans
        return ans


number_fib_calls = 0
fib_args = 10

# print(fib(fib_args))
# print('function calls', number_fib_calls)

number_fib_calls = 0

# print(fib_efficient(fib_args))
# print('function calls', number_fib_calls)

#EXERCISE 4###############################################################################3

#1 Write a function that reads the words in words.txt and stores them as keys in a dictionary. It doesn???t matter what the values are. Then you can use the in operator as a fast way to check whether a string is in the dictionary.

x = {}
def dictionarykeys(word):
    f = open('data/random_words.txt')
    for i in f:
        i = i.strip()
        x[i] = ''
    if word in x:
        return True

# print(dictionarykeys('zemindar'))


#2 Write a function named has_duplicates that takes a list as a parameter and returns True if there is any object that appears more than once in the list.
def has_duplicates(s):
    """Returns True if any element appears more than once in a sequence.
    """
    if len(s) == len(set(s)):
        return False
    else:
        return True

