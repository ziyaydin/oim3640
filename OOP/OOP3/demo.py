import random
# class Covid:
#     """This is a class of Covid. Each covid should have a base sequence, and extension"""
#     base_sequence = "abcd"
#     def __init__(self, new_seq="###"):
#             self.extension = new_seq
#             self.sequence = self.base_sequence + self.extension

#     def replicate(self):
#         """ return a new covid instance by replicating itself"""
#         return Covid(self.extension)

#     def __add__(self, another_covid):
#         """ return a new covid instance by mixing self and another covid """
#         new_seq = ''.join(random.choices(self.extension, another_covid.extension, 3))
#         return Covid(new_seq)

#     def __str__(self):
#         """ represent the instance in a human-readable format"""
#         return f'{self.name}: {self.sequence}'


# covid_0 = Covid() #creating an istance of Covid by invoking the initializer method, __init__
# covid_1 = Covid("123")

# print(covid_0.sequence)
# print(covid_1.sequence)
# covid_2 = covid_1.replicate()
# print(covid_2.sequence)
# # print(covid_2.mix(covid_0).sequence)
# print(covid_0 + covid_2)

import random


class Covid:
    """This is a class of Covid. Each covid should have a name, a base sequence, and extension"""

    base_sequence = "abcd"

    def __init__(self, name="unknown covid", new_seq="###"):
        self.name = name
        self.extension = new_seq
        self.sequence = self.base_sequence + '.' + self.extension

    def replicate(self):
        """return a new Covid instance by replicating itself"""
        return Covid(
            name="replicated " + self.name, new_seq=self.extension
        )  # means call __init__(self, new_seq=self.extension)

    def __add__(self, another_covid):
        """ Overloading the + operator
        return a new Covid instance by mixing self and another covid"""
        new_seq = ''.join(random.choices(self.extension + another_covid.extension, k=3))
        return Covid(name='New Covid from Mixing', new_seq=new_seq)

    def __str__(self):
        """ This method makes print(object) available
        represent the instance in a human-readable format"""
        return f'{self.name}: {self.sequence}'


covid_0 = Covid(name='Ground zero')
# creating an instance of Covid by invoking the initializing method, __init__

covid_1 = Covid(name='second case', new_seq="123")

print(covid_0)
print(covid_1)
covid_2 = covid_1.replicate()
print(covid_2)
# print(covid_2.mix(covid_0).sequence)
covid_3 = covid_0 + covid_2
print(covid_3)