#used code of https://github.com/OIM3640/oim3640/blob/main/OOP/OOP2/Time1_solution.py

class Time:
    """Represents the time of day.
    attributes: hour, minute, second
    """


time = Time()  # create an instance of Time type
time.hour = 3
time.minute = 12
time.second = 30

print(time.hour, time.minute, time.second)

later = Time()
later.hour = time.hour
later.minute = time.minute + 5
later.second = time.second

print(later.hour, later.minute, later.second)


"""""" """""" """""" """""" """""" """"""
# Exercise 1
"""""" """""" """""" """""" """""" """"""

# create a function print_time
def print_time(t):
    """Prints a string representation of the time.
    t: Time object
    """
    print(f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}')


print_time(time)
print_time(later)


def is_after(t1, t2):
    """Returns True if t1 is after t2; false otherwise."""
    return (
        t1.hour > t2.hour
        or (t1.hour == t2.hour and t1.minute > t2.minute)
        or (t1.hour == t2.hour and t1.minute == t2.minute and t1.second > t2.second)
    )


print(is_after(time, later))
print(is_after(later, time))


"""""" """""" """""" """""" """""" """"""
# Prototyping
"""""" """""" """""" """""" """""" """"""


def add_time(t1, t2):
    """Adds two time objects.
    t1, t2: Time
    returns: Time
    TODO: improve this function
    """
    sum_time = Time()
    sum_time.hour = t1.hour + t2.hour
    sum_time.minute = t1.minute + t2.minute
    sum_time.second = t1.second + t2.second
    return sum_time


def add_time2(t1, t2):
    """Adds two time objects.
    t1, t2: Time
    returns: Time
    TODO: improve this function # DONE!
    """
    sum_time = Time()
    sum_time.hour = t1.hour + t2.hour
    sum_time.minute = t1.minute + t2.minute
    sum_time.second = t1.second + t2.second
    if sum_time.second >= 60:
        sum_time.second -= 60
        sum_time.minute += 1
    if sum_time.minute >= 60:
        sum_time.minute -= 60
        sum_time.hour += 1
    return sum_time


# Uncomment below for testing
# start = Time()
# start.hour = 9
# start.minute = 45
# start.second = 0

# duration = Time()
# duration.hour = 1
# duration.minute = 35
# duration.second = 0

# done = add_time2(start, duration)
# print_time(done)


def increment(time, seconds):
    """Adds seconds to a Time object."""
    time.second += seconds

    if time.second >= 60:
        time.second -= 60
        time.minute += 1

    if time.minute >= 60:
        time.minute -= 60
        time.hour += 1


"""""" """""" """""" """""" """""" """"""
# Exercise 3
"""""" """""" """""" """""" """""" """"""


def increment_2(time, seconds):
    """return a Time object after incrementing"""
    result = Time()
    result.hour, result.minute, result.second = time.hour, time.minute, time.second
    result.second += seconds
    if result.second >= 60:
        result.second -= 60
        result.minute += 1
    if result.minute >= 60:
        result.minute -= 60
        result.hour += 1
    return result


"""""" """""" """""" """""" """""" """"""
# Designed Development
"""""" """""" """""" """""" """""" """"""


def time_to_int(time):
    """Computes the number of seconds since midnight.
    time: Time object.
    """
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds


def int_to_time(seconds):
    """Makes a new Time object.
    seconds: int seconds since midnight.
    """
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


def add_time_2(t1, t2):
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)


"""""" """""" """""" """""" """""" """"""
# Exercise 4
"""""" """""" """""" """""" """""" """"""


def substract_time(t1, t2):
    """Substracts two time objects.
    t1, t2: Time
    returns: Time
    """
    seconds = time_to_int(t1) - time_to_int(t2)
    return int_to_time(seconds)


# print_time(substract_time(done, duration))
# print_time(substract_time(time, later))


"""""" """""" """""" """""" """""" """"""
# Error handling
"""""" """""" """""" """""" """""" """"""


def valid_time(time):
    """Checks whether a Time object satisfies the invariants.
    time: Time
    returns: boolean
    """
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.second >= 60:
        return False
    return True


def add_time3(t1, t2):
    """Adds two time objects.
    t1, t2: Time
    returns: Time
    """
    # assert valid_time(t1) and valid_time(t2)

    if not valid_time(t1) or not valid_time(t2):
        raise ValueError('invalid Time object in add_time, stupid!')
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)


# done = add_time3(start, duration)
# print_time(done)
# another = add_time3(done, duration)
# print_time(another)


"""""" """""" """""" """""" """""" """"""
# Exercise 5
"""""" """""" """""" """""" """""" """"""


def mul_time(t1, factor):
    """Multiplies a Time object by a factor."""
    if not valid_time(t1):
        raise ValueError('invalid Time object in mul_time, stupid!')
    seconds = time_to_int(t1) * factor
    return int_to_time(int(seconds))


# print_time(duration)
# print('after multiplied by 5:', end=' ')
# print_time(mul_time(duration, 5))


def main():
    # if a movie starts at noon...
    noon_time = Time()
    noon_time.hour = 12
    noon_time.minute = 0
    noon_time.second = 0

    print('Starts at', end=' ')
    print_time(noon_time)

    # and the run time of the movie is 109 minutes...
    movie_minutes = 109
    run_time = int_to_time(movie_minutes * 60)
    print('Run time', end=' ')
    print_time(run_time)

    # what time does the movie end?
    end_time = add_time2(noon_time, run_time)
    print('Ends at', end=' ')
    print_time(end_time)

    print('Does it end after it begins?', end=' ')
    print(is_after(end_time, noon_time))

    print('Home by', end=' ')
    travel_time = 600  # 10 minutes
    home_time = increment_2(end_time, travel_time)
    print_time(home_time)

    race_time = Time()
    race_time.hour = 1
    race_time.minute = 34
    race_time.second = 5

    print('Half marathon time', end=' ')
    print_time(race_time)

    distance = 13.1  # miles
    pace = mul_time(race_time, 1 / distance)

    print('Time per mile', end=' ')
    print_time(pace)


# if __name__ == '__main__':
#     main()
