#Ex 1.2
def sum1000():
    result = 0 # the initial value
    for i in range(1, 1001):
        print(f'Iteration {i}:')
        print(f' Before adding {i}, current result is {result}.')
        result = result + i #result += 1
        print(f' after adding {i}, result becomes {result}. \n')

    print(result)

#sum(1000)

#Ex 1.3

def sum_odd():
    """ """
    result = 0

    for i in range(1, 1001):
        if i % 2 == 1:
            result += i

    return(result)

# print(sum_odd())

def sum_odd_2():
    result = 0
    for i in range(1, 1001, 2):
        result += i
    return result

# print(sum_odd_2())

################################# WHILE LOOP
def countdown(n):
    while n > 0:
        print(n)
        n = n - 1
    print('Blastoff!')

# When the part after while correct, do the bottom things

# iteration = 0
# count = 0
# while iteration < 5:
#     # the variable 'letter' in the loop stands for every 
#     # character, including spaces and commas!
#     for letter in "hello, world": 
#         count += 1
#     print("Iteration " + str(iteration) + "; count is: " + str(count))
#     iteration += 1 



def countdown(n):
    while n > 0:
        print(n)
        n = n - 1
    print('Blastoff!')

# countdown(20)

# iteration = 0
# count = 0
# while iteration < 5:
#     # the variable 'letter' in the loop stands for every 
#     # character, including spaces and commas!
#     for letter in "hello, world":
#         count = count + 1
#     print("Iteration " + str(iteration) + "; count is: " + str(count))
#     iteration += 1 

i = 0
while (i <= 100):
    i += 1
    print(i)



# iteration = 0
# while iteration < 5:
#     count = 0
#     for letter in "hello, world":
#         count += 1
#     print("Iteration " + str(iteration) + "; count is: " + str(count))
#     iteration += 1 

# iteration = 0
# while iteration < 5:
#     count = 0
#     for letter in "hello, world":
#         count += 1
#         if iteration % 2 == 0:
#             break
#     print("Iteration " + str(iteration) + "; count is: " + str(count))
#     iteration += 1 

# ###EXERCISE 03
# import sys #For epilson
# import math
# from tabulate import tabulate

# def mysqrt(z):
#     x = z/2
#     while True:
#         print(x)
#         y = (x + z/x) / 2
#         if abs(y-x) < sys.float_info.epsilon: #Got help from https://stackoverflow.com/questions/9528421/value-for-epsilon-in-python
#             break
#     x = y

# # def the_sqrt_table():
# #     a = float(input('choose the start value'))
# #     for i in range(10):1
# #         print(a)
# #         alpha = mysqrt(a)
# #         print(alpha)
# #         beta = math.sqrt(a)
# #         print(beta)
# #         print(abs(alpha - beta)) 

# # the_sqrt_table()

# a = float(input('choose the start value'))

# d = [ [a],
#      [ mysqrt(a)],
#      [math.sqrt(a)]
#      [mysqrt(a) - math.sqrt(a)]]

# print(tabulate(d, headers=["a", "mysqrt", "math.sqrt", "difference"]))


# defa = 0
# def harf():
#     harf_sayisi = 0
#     for harf in 'ziya':
#         harf_sayisi += 1
#         print(harf)
#         print(harf_sayisi)



# harf()
# defa = 0
# harfsayisi = 0
# while defa < 5:
#     # the variable 'letter' in the loop stands for every 
#     # character, including spaces and commas!
#     for harf in "hello, world": 
#         harfsayisi += 1
#     print("ninci defa " + str(defa) + "; harfsayisi is: " + str(harfsayisi))
#     defa += 1 