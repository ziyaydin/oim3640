# ex_06
import math


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
