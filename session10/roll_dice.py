# roll a dice, random integers 1 - 6
# roll dice 100 times
# repeat 10 times

# Function 1 -roll 100 dice and print the sum
        # 1.create a variable to store sum, result, initilized at 0
        # 2 import random librray
        # 3. repeat the following stpes by 100 times:
            # get a random integers in range 1 to 6 
            # add the random integer to result
        # 4. print the result
# Function 2 - repeat the simulation 10 times
        # 1. repeat the dollowing steps 10 times
            #function 1

import random

def simulation(num_dice=100):
    """ roll 100 dice and print the sum"""
    result = 0
    for i in range(100):
        result += random.randint(1, 6)
    print(result, result/num_dice)

# simulation() #expected value

def repeat_simulations(n):
    """repeat simulation n times"""
    for i in range(n):
        simulation()

repeat_simulations(10)