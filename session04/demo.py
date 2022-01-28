# # TODO: use this function to edit your code when necessary

import random
import math
print(len(str(2 ** 10)))

print(math.pi)

print(random.random())
random.choice([1, 2, 3, 4])

print('I\'m \"ok\".')  # Use escape character \
print('I\'m learning\nPython.')
print('\\\n\\')

print('\\\t\\')
print(r'\\\t\\')

print('''line1
... line2
... line3''')

# print(3>2)
in_China = False
age = int(input('How old are you? >>>'))
# age = int(age)
if age > 21 or in_China:
    print('Yes, you can.')
else:
    print('No, you cannot.')


def f():
    print('hi')


result = f()
print(result)
