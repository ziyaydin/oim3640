"""
Question 1:

Write a function that prompts the user for a weight on earth and prints the equivalent weight on the moon (16.5%)

Weight on Moon = weight on Earth * 0.165

Notice:
1. Please write pseudo-code before coding the function.
2. Your function should include docstring.
3. Write your own test code, i.e. call the function.
"""

def weight():
    """
    this function takes your weight on earth and converts it to your weight in moon
    input: your weight on earth
    """
    #1.Ask the weight of the perosn on earth
    #  Convert it to your weight in moon by multiplying with 16.5%
    #  Print the weight in moon  
    weight = int(input('What is your weight on earth:'))
    print('Your weight in moon is', weight * 0.165)

weight()

