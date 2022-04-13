#used code from https://github.com/OIM3640/oim3640/blob/main/OOP/OOP2/datetime_exercise_solution.py
from datetime import datetime

def days_until_birthday(birthday):
    """How long until my next birthday?"""
    today = datetime.today()
    # when is my birthday this year?
    next_birthday = datetime(today.year, birthday.month, birthday.day)

    # if it has gone by, when will it be next year
    if today > next_birthday:
        next_birthday = datetime(today.year + 1, birthday.month, birthday.day)

    # subtraction on datetime objects returns a timedelta object
    delta = next_birthday - today
    return delta.days


def double_day(b1, b2):
    """Compute the day when one person is twice as old as the other.
    b1: datetime birthday of the younger person
    b2: datetime birthday of the older person
    """
    assert b1 > b2
    delta = b1 - b2
    dday = b1 + delta
    return dday


def datetime_exercises():
    """Exercise solutions."""

    # print today's day of the week
    today = datetime.today()
    print(today.weekday())
    print(today.strftime('%A'))

    # compute the number of days until the next birthday
    # (note that it usually gets rounded down)
    birthday = datetime(1999, 7, 4)
    print('Days until birthday', end=' ')
    print(days_until_birthday(birthday))

    # compute the day one person is twice as old as another
    b1 = datetime(2019, 12, 26)
    b2 = datetime(2000, 11, 5)
    print('Double Day', end=' ')
    print(double_day(b1, b2))


def main():
    datetime_exercises()


if __name__ == '__main__':
    main()