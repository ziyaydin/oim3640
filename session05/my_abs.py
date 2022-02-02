# ex_03
import math


def my_abs(number):
    """print the absolute value of the given number"""
    if number < 0:
        print(-number)
    else:
        print(number)


my_abs(-100)
my_abs(100)

# ex_04


def my_abs_2(number):
    """return the absolute value of the given number"""
    if number < 0:
        return -number
    else:
        return number


x = my_abs_2(-80)
print(my_abs_2(x))
print(my_abs_2(-50))

# ex_05


def my_abs_3(number):
    """if number is an integer or float take the absolute vallue, if it something else say BYE"""
    if isinstance(number, int):
        return my_abs_2(number)
    elif isinstance(number, float):
        return my_abs_2(number)
    else:
        return 'Bye'


print(my_abs_3('ziya'))
print(my_abs_3(-508))

# #ex_06


def quadratic(a, b, c):
    """solves the quadratic equation, the format of ax^2 + bx + c = 0 """
    discriminant_of_polynomial = b * b - 4 * a * c
    sqrt_part = math.sqrt(abs(discriminant_of_polynomial))
    if discriminant_of_polynomial > 0:
        print((-b + sqrt_part) / (2 * a), (-b - sqrt_part) / (2 * a))
    elif discriminant_of_polynomial == 0:
        print(-b / (2 * a))
    else:
        print('Sorry, I miss this class in highschool. I can\'t remember what happens when the discriminant of the polynomial is less than 0 :(')

quadratic(1, -3, 2)
quadratic(1, 3, 4)
quadratic(1, 3, -4)