"""
Question 1:

Write a function that prompts the user for a weight on earth and prints the equivalent weight on the moon (16.5%)

Weight on Moon = weight on Earth * 0.165

Notice:
1. Please write pseudo-code before coding the function.
2. Your function should include docstring.
3. Write your own test code, i.e. call the function.
"""

from time import monotonic


def weight():
    """
    this function takes your weight on earth and converts it to your weight in moon
    input: your weight on earth
    """
    #1.Ask the weight of the perosn on earth
    #  Convert it to your weight in moon by multiplying with 16.5%
    #  Print the weight in moon  
    weight = float(input('What is your weight on earth:'))
    print('Your weight in moon is', weight * 0.165)

# weight()

"""
Question 2:
Write a function that takes two arguments - 1. weight on earth (float), 2. planet (str) - and returns the equivalent weight on that planet. We assume Moon is a planet although it is not.
Weight on Moon = weight on Earth * 0.165
Weight on Mars = weight on Earth * 0.378
Weight on Jupiter = weight on Earth * 2.528
Notice:
1. Please write pseudo-code before coding the function.
2. Your function should include docstring.
3. Write your own test code, i.e. call the function.
"""

def weight_2():
    """
    this function takes your weight on earth
    then converts your earth weight to the weight of another planet"""
    #1. ask the weight of on earth
    #2. ask the which planet they are at
    #3. return the the weight in the appropriate planet
    weight = float(input('What is your weight on earth:'))
    planet = str(input('what planet you are at: (plase make the first letter of the planet capital)'))
    if planet == 'Moon':
        return(weight * 0.165)
    elif planet == 'Mars':
        return(weight * 0.378)
    elif planet == 'Jupiter':
        return(weight * 2.528)
    else:
        print('Sorry, don\'t know that planet')

# print(weight_2())

def weight_3(weight, planet):
    """This function takes your weight on earth and converts to the weight in another planet"""
    if planet == 'Moon':
        return(weight * 0.165)
    elif planet == 'Mars':
        return(weight * 0.378)
    elif planet == 'Jupiter':
        return(weight * 2.528)
    else:
        print('Sorry, don\'t know that planet')

print(weight_3(100, 'Moon'))
