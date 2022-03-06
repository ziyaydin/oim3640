# #A bad word should:
# - contain at least three letters from "covid",
# - and contain at least one letter that occurs twice in a row,
# - and have same first letter and last letter. 


def uses_only(word, available):
    """
    takes a word and a string of letters, and that returns True if the word
    contains only letters in the string available.
    """
    for letter in word: 
        if letter not in available:
            return False
    return True

def find_words_only_use_covid(word): 
    """This function creates words that only has the letters of "planet" 
    """
    words_with_covid= 0 
    word = word.strip()
    if uses_only(word,'covid'):
        words_with_covid +=1
    if words_with_covid >= 3:
        return True
    else:
        return False

def has_adjacent_duplicates(s):
    """Returns True if there are two same adjacent elements.

    s: string or list

    returns: bool

    output:
    >>> print(has_adjacent_duplicates('cba'))
    False
    >>> print(has_adjacent_duplicates('abca'))
    Flase
    >>> print(has_adjacent_duplicates('abbc'))
    True
    """
    for element in range(len(s) -1 ): #DONT FORGET THE -1 FOR THE LAST CHARACTER
        if s[element] == s[element +1]:
            return True
    return False

def same_last_same_first(word):
    if word[0] == word[-1]:
        return True
    else:
        return False

def bad_word():
    """ 
    """
    f = open('data/random_words.txt')  #we need this to look at randomword data file
    for i in f:
        # if find_words_only_use_covid == True:
        #     if has_adjacent_duplicates == True:
        if same_last_same_first == True:
            print(i)

print(bad_word())
