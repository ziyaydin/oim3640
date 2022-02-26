
# Assume words.txt is under data folder
# f = open('data/words.txt')
# line = f.readline()
# print(line)


# f = open('data/words.txt')

# number_of_words = 0

# for line in f:
#     word = line.strip()
#     number_of_words += 1

# print(number_of_words)


def find_long_words():
    """
    prints only the words with more than 20 characters
    """
    f = open('data/words.txt')  # Assume words.txt is under data folder

    for line in f:
        word = line.strip()
        if len(word) > 20:
            print(word, len(word))


# find_long_words()


def has_no_e(word):
    """
    returns True if the given word doesn’t have the letter "e" in it
    """    
    for letter in word:
        if letter.lower() == 'e':
            return False
    return True


# print(has_no_e('Babson'))
# print(has_no_e('College'))
# print(has_no_e('EA sports'))


def find_words_no_e():
    """
    returns the percentage of the words that don't have the letter "e"
    """
    f = open('data/words.txt')  # Assume words.txt is under data folder
    num_words_no_e = 0
    num_words = 0
    for line in f:
        word = line.strip()
        if has_no_e(word):
            num_words_no_e += 1
        num_words += 1
    return num_words_no_e / num_words


# perc_no_e = find_words_no_e()
# print(f'The percentage of the words with no "e" is {perc_no_e*100:.2f}%.')


def avoids(word, forbidden):
    """
    returns True if the given word does not use any of the forbidden letters
    """
    for letter in word:
        if letter == forbidden:
            return False
    return True


# print(avoids('Babson', 'abcde'))
# print(avoids('College', 'e'))
# print(avoids('Boston', 'xyz'))


def find_words_no_vowels():
    """
    returns the percentage of the words that don't have vowel letters
    """
    f = open('data/words.txt')  # Assume words.txt is under data folder

    num_words_yes_vowel = 0
    num_words = 0
    for letter in f:
        letter = letter.strip()
        if 'a' in letter:
            num_words_yes_vowel += 1
        elif 'e' in letter:
            num_words_yes_vowel += 1
        elif 'i' in letter:
            num_words_yes_vowel += 1
        elif 'o' in letter:
            num_words_yes_vowel += 1
        elif 'u' in letter:
            num_words_yes_vowel += 1
        num_words += 1
    return 1 - (num_words_yes_vowel / num_words)

perc_no_vowel = find_words_no_vowels()
# print(f'The percentage of the words without vowel letters is {perc_no_vowel*100:.2f}%.')


def uses_only(word, available): #Got help from https://github.com/OIM3640/resources/blob/main/notebooks/09%20-%20Case%20-%20Word%20Play.ipynb
    """
    takes a word and a string of letters, and that returns True if the word
    contains only letters in the string available.
    """
    for letter in word:
        if letter not in available:
            return False
    return True


# print(uses_only('Babson', 'aBbsonxyz'))
# print(uses_only('college', 'aBbsonxyz'))
# print(uses_only('ziya', 'ayiz'))


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

# print('Number of words that use only letters from "planets" is', find_words_only_use_planet())


def uses_all(word, required): #Got help from https://github.com/OIM3640/resources/blob/main/notebooks/09%20-%20Case%20-%20Word%20Play.ipynb
    """
    takes a word and a string of required letters, and that returns True if
    the word uses all the required letters at least once.
    """
    for letter in required: 
        if letter not in word:
            return False
    return True

# print(uses_all('Babson', 'aBbsonxyz'))
# print(uses_all('college', 'aBbsonxyz'))
# print(uses_all('ziya', 'ayiz'))
# print(uses_all('duck', 'duck'))

def find_words_using_all_vowels():
    """
    return the number of the words that use all the vowel letters
    """
    f = open('data/words.txt')  # Assume words.txt is under data folder
    number_words_with_all_vowels = 0
    for word in f:
        word = word.strip()
        if uses_all(word,'aeiou'):
            number_words_with_all_vowels += 1
    return number_words_with_all_vowels

# print('The number of words that use all the vowels:', find_words_using_all_vowels())


def is_abecedarian(word):
    """
    returns True if the letters in a word appear in alphabetical order
    (double letters are ok).
    """
#My code Using sorted
    # word = list(word) #makes the word  as alist to sort them alphabetically in the next step
    # alphabetical_order = sorted(word) #sorted means that alphabtically sorted. 
    # if word == alphabetical_order:
    #     # print(word) #To visualize that word is and what alphabtical_order is 
    #     # print(alphabetical_order)
    #     return True
    # else:
    #     # print(word)
    #     # print(alphabetical_order)
    #     return False
#Mycode
    letter_place = 0
    for letters in range(len(word)-1):
        letter_place += 1
        if ord(word[letter_place]) > ord(word[letter_place + 1]):
            return 'False'
        else:
            return 'True'
# # Professors code:
#     for i in range(len(word)-1):
#         if word[i+1] < word[i]:
#             return False
#         return True


print(is_abecedarian('abs'))
print(is_abecedarian('college'))
print(is_abecedarian('aaabcdef'))

def find_abecedarian_words():
    """
    returns the number of abecedarian words
    """
    f = open('data/words.txt')  # Assume words.txt is under data folder
    number_of_abc_words= 0
    for word in f:
        word = word.strip()
        if is_abecedarian(word) == True:
            number_of_abc_words += 1
    return number_of_abc_words

# print(find_abecedarian_words())


def is_abecedarian_using_recursion(word): #I cant understand recursion :(
    """
    returns True if the letters in a word appear in alphabetical order
    (double letters are ok).
    """
    pass


# print(is_abecedarian_using_recursion('abcdef'))


def is_abecedarian_using_while(word):
    """
    returns True if the letters in a word appear in alphabetical order
    (double letters are ok).
    """
    pass

# print(is_abecedarian_using_while('abcdef'))