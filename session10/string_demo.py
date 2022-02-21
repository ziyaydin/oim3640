team = 'New England Patriots'
# letter = team[1] 
# # print(letter)
# last = team[-1]
# # print(last)

# for letter in team:
#     print(letter, end='')

#Exercise 01
# prefixes = 'JKLMNOPQ'
# suffix = 'ack'
# for letter in prefixes:
#     if prefixes == 'O' or letter == 'Q':
#         print(letter + 'u' + suffix)
#     else:
#         print(letter + suffix)


def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

# print(find(team, 'E'))

word = 'New England Patriots'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
# print(count)

#Exercise 02
def count(word, letter):
    index = 0
    for letters in word:
        if letters == letter:
            index = index + 1
    print(index)

# count(team, 'a')

team = 'New England Patriots'
new_team = team.upper()
# print(new_team)

team = 'New England Patriots'
index = team.find('a')
# print(index)

# print(team.find('En'))
# print(team.find('a', 10)) 

def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False
# any_lowercase1('ZIYA')

def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'
# any_lowercase2('ZIYA')

def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag
# any_lowercase3('ZIYA')

def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag
# any_lowercase4('ZIYA')

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True
# any_lowercase5('ZIYA')

# #Exercise 05
new_word = 'cheer'
def rotate_word(new_word, number):
    #1. transform every letter to a number by using ord function
    #2. add the number to every letter
    #3. transform every number to a character with chr funcion
    #4. print the new  word
    """ takes the word(string) and rotates the letter by number(integer)"""
    for letters in new_word:
        print(chr(ord(letters) + number))

rotate_word(new_word, 7)

