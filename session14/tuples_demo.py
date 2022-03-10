t = 'a', 'b', 'c', 'd', 'e'
t = ('a', 'b', 'c', 'd', 'e')
# print(t[0])
# print(t[1:3])

a = 10
b = 90
temp = a
a = b
b = temp
# print(a, b)
a, b = b, a

email = 'zli@babson.edu'
id, domain = email.split('@')
# print(id)
# print(domain)

t = divmod(7, 3)
# print(t)

# def printall(*args):
# # print(args)
    
# printall(1, 2.0, '3')
# printall(1, 2.0, '3', None, True)

######################Exercise 2.2
#Write a program that reads a word list from a file and prints all the sets of words that are anagrams.
# """
# Pseudo-code
#DONE 1. read words.txt into a list of words DONE
#DONE 2. sort one word, convert the word to a sorted tuple/string
# e.g.
# 'spot' -> 'opts'
# 'ba' -> 'ab'
#WIP 3. create a dictionary, key is the sorted tuple/string, value is a list of anagram words  
# e.g.
# {'ab': ['ab', 'ba'], 'opts': ['spot','pots']}
# 4. create a new list, by getting the values of dict only - we only want the lists that have more than one word. and return the list
# 5. print the list

# """


def sorter(w): # 2. sort one word, convert the word to a sorted tuple/string
    """
    sorts the letters in the word in alphabetical order
    """
    t = sorted(w)
    t = ''.join(t)
    t = list(w)
    return t
print(sorter('ziya'))

def anagram_finder(): #3. create a dictionary, key is the sorted tuple/string, value is a list of anagram words  
    f = open('data/words.txt')
    d = {}
    for line in f:
        word = line.strip #strip it to get rid of unseen cahracters
        t = sorter(word) #sorter function to sort the letters
        if t not in d:
            d[t] = [word]
        else:
            d[t].append[word] #if sorted letters (t) is not in the dictionary (d) add the word to dictionary
    # print(d)

def print_anagram_sets(d):
    """Prints the anagram sets in d.
    d: map from words to list of their anagrams
    """
    for v in d.values():
        if len(v) > 1:
            print(len(v), v)

# anagram_finder()


def print_anagram_sets(d):
    """Prints the anagram sets in d.
    d: map from words to list of their anagrams
    """
    for v in d.values():
        if len(v) > 1:
            print(len(v), v)

with open('words.txt') as f:
        x = f.read().split()
        y = []
        c =[]
        sortedc = []
        anagrams = {}
        counter = 0
        for i in x:
                y.append(sorted(i))  
        for word in y:
                anagrams[''.join(word)] = 1
                sortedc.append(''.join(word))
print(sorted(sortedc))


def is_anagram(word1, word2):
    """Checks whether two words are anagrams
    """
    if sorted(word1) == sorted(word2):
        return True
    else:
        return False
