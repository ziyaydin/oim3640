# EX2.2
from cmath import sqrt
import math
# Calculate the sum of integers from 1 to 10. WITH WHILE LOOP
def sum_from_0_to(ceiling_number):
    """ prints the sum of numbers from 0 to ceiling_number """
    summ = 0
    new_number = 1
    while new_number <= ceiling_number:
        summ = summ + new_number
        new_number = new_number + 1
    print(summ)

    if ceiling_number * (ceiling_number + 1) / 2 == summ:
        print("double check succesful")
    else:
        print("something is wrong")

# sum_from_0_to(10)

# Calculate the sum of integers from 1 to 1000. (hint: we need to use range().) WITH WHILE LOOP


def sum_from_0_to(ceiling_number):
    """ prints the sum of numbers from 0 to ceiling_number """
    summ = 0
    new_number = 1
    while new_number <= ceiling_number:
        summ = summ + new_number
        new_number = new_number + 1
    print(summ)

    if ceiling_number * (ceiling_number + 1) / 2 == summ:
        print("double check succesful")
    else:
        print("something is wrong")

# sum_from_0_to(1000)


# Calculate the sum of all the odd numbers from 1 to 1000. (hint: check out range() function in Python documentation.) How about all the even numbers? WITH WHILE LOOP

def sum_of_odds_from_0_to(ceiling_number):
    """ prints the sum of numbers from 0 to ceiling_number """
    summ = 0
    new_number = 1
    while new_number <= ceiling_number:
        if new_number % 2 == 1:
            summ = summ + new_number
        new_number = new_number + 1
    print(summ)
# sum_of_odds_from_0_to(100)

# EX 3 TODO: I need to learn a better way to print as a table. Proper columns etc
# TODO: How can i print this at once for multiple a values in a proper table 
def newtons_method(a):
    x = a/2
    while True:
        y = (x + a/x) / 2
        if abs(y-x) < 0.0000001:
            break
        x = y
    print( "a", "mysqrt(a)", "math.sqrt(a)", "  diff")
    print( a, "   ", round(x,2), "   " , math.sqrt(a),"         ", round((x - math.sqrt(a)),2))

newtons_method(9)

