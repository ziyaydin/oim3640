# def gd():
#     print('Beginning of GH day')
#     import time
#     time.sleep(1)
#     print('End of GH day')
#     time.sleep(2)
#     gd()
###################3# FUNCTIONS#########################3

import math


r1 = 20.16
r2 = 9.13
r3 = 11.55

# a1 = 3.14 * r1 * r1
# a2 = 3.14 * r2 * r2
# a3 = 3.14 * r3 * r3

# print(a1, a2, a3)


def area_of_circle(r):
    """print the area of a circle given the radius value"""
    area = math.pi * r * r
    print(area)


area_of_circle(r1)
area_of_circle(r2)
area_of_circle(r3)


def print_lyrics():
    print("Hey Jude. Don't make it bad.")
    print("Take a sad song and make it better.")
type(print_lyrics)
print_lyrics()

# def give_me_a_break():
#     str1 = 'break'
#     return str1
# print(give_me_a_break())

def give_me_a_break():
    str1 = 'break'
    return str1
    print('another break')
    
print(give_me_a_break())


