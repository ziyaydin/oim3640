# fout = open('data/dylan.txt', 'a')

# line1 = "How many roads must a man walk down\n"
# fout.write(line1)

# line2 = "Before you call him a man?\n"
# fout.write(line2)

# fout.close()

# with open('data/dylan.txt', 'w') as fout:
#     line1 = "How many roads must a man walk down\n"
#     fout.write(line1)
#     line2 = "Before you call him a man?\n"
#     fout.write(line2)

import os
cwd = os.getcwd() 

def walk(dirname):
    """Prints the names of all files in 
    dirname and its subdirectories.

    dirname: string name of directory
    """
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)

        if os.path.isfile(path):
            print(path)
        else:
            walk(path)


# try:
#     f = open('data/data.txt')

# except FileNotFoundError as e:
#     with open('data/data.txt') as f:

import pickle

d = {'a': 1, 'b':2, 'c':3}
t = [1, 2, 3]
# print(pickle.dumps(t))

# with open('data/d.txt', "w") as f:
#     f.write(d)

# t1 = [1, 2, 3]
# s = pickle.dumps(t1)
# t2 = pickle.loads(s)
# print(t2)
# t1 == t2
# t1 is t2
