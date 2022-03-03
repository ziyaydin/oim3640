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

def find_words_only_use_planet(): 
    """This function creates words that only has the letters of "planet" 
    """
    f = open('data/words.txt')  # Assume words.txt is under data folder
    words_with_planets= 0 
    for word in f:
        word = word.strip()
        if uses_only(word,'planets'):
            words_with_planets +=1
    return words_with_planets

def bad_word():
    """ 
    """
    f = open('data/random_words.txt')  #we need this to look at randomword data file
    bad = 0
    for word in f: #USES LETTERS FROM COVID AT LEAST ONCE
        if uses_only(word, 'covid'):
            bad += 1
            return bad
        for letters in word:
            if word[letters] == word[letters + 1]: #WIP
        pass
