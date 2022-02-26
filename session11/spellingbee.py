
def uses_only(word, available):
    """
    takes a word and a string of letters, and that returns True if the word
    contains only letters in the string available.
    """
    for letter in word: 
        if letter not in available:
            return False
    return True


def spelling_bee(center_letter, required_letters): 
    """ 
    This function takes the center letter, and creates 4 or more letter words using some or all of the letters from the required letters. The source of the data is words.txt
    """
    f = open('data/words.txt')  # Assume words.txt is under data folder
    for word in f:
        word = word.strip()
        if center_letter in word: 
            if uses_only(word, required_letters + center_letter) and len(word) > 3:
                print(word)

spelling_bee('o', 'ikptch')



