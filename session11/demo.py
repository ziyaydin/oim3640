# how many vowels in a name

count = 0
def vowelcounter(name):
    count = 0
    for letter in name:
        if letter in 'aeiou':
            count += 1
    print(count)

vowelcounter('ziyaaa')


def mvowelcounter(names):
    count = 0
    for i in names:
        if i == 'a' or i == 'i':
            count += 1
    print(count)

# mvowelcounter('ziya')


def evenintegers():
    n = 2
    sum = 0
    while 2 <= n <= 2022:
        if n % 2 == 0:
            sum += n
        n += 1
    return sum / n

# print(evenintegers())
