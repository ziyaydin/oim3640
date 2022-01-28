# 3. The time module provides a function, also named time, that returns the current Greenwich Mean Time in “the epoch”, which is an arbitrary time used as a reference point. On UNIX systems, the epoch is 1 January 1970.

import time
# This is for Greenwich, UK and The epoch is 1 January 1970
time_since_epoch = time.time()

number_of_days = int(time_since_epoch / 3600 / 24)
print(f'{number_of_days:.0f} days passed since epoch')


seconds = time_since_epoch % (60 * 60 * 24)

hour_in_gw = int(seconds/(60 * 60))
hour_in_boston = hour_in_gw + 7
minutes = int(seconds/60)
minute_right_now = minutes % 60
second_right_now = int(seconds % 60)

print('In Boston, right now it is', hour_in_boston, '.',
      minute_right_now, '.', second_right_now, 'PM')
