t = 'a', 'b', 'c', 'd', 'e'
t = ('a', 'b', 'c', 'd', 'e')
# print(t[0])
# print(t[1:3])

a = 10
b = 90
temp = a
a = b
b = temp
# print(a, b)
a, b = b, a

email = 'zli@babson.edu'
id, domain = email.split('@')
# print(id)
# print(domain)

t = divmod(7, 3)
# print(t)

def printall(*args):
    print(args)
    
# printall(1, 2.0, '3')
# printall(1, 2.0, '3', None, True)