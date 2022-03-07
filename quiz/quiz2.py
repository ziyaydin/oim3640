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

# print(find_words_only_use_covid('babcovidbab'))

def has_adjacent_duplicates(s):
    """Returns True if there are two same adjacent elements.
    """
    for element in range(len(s) -1 ): #DONT FORGET THE -1 FOR THE LAST CHARACTER
        if s[element] == s[element +1]:
            return True
    return False

# print(has_adjacent_duplicates('Babsonna'))

def same_last_same_first(word):
    if word[0] == word[-1]:
        return True
    else:
        return False

def bad_word():
    """ 
    prints the words 
    that contain at least three letters from "covid",
    and contain at least one letter that occurs twice in a row,
    and have same first letter and last letter. 
    
    """
    f = open('data/random_words.txt')  #we need this to look at randomword data file
    for i in f:
        i = i.strip()
        if same_last_same_first(i) == True:
            if has_adjacent_duplicates(i) == True:
                if find_words_only_use_covid(i) == True:
                    print(i)

bad_word()
