from BabsonPerson import BabsonPerson
from Student import Student
from Person import Person


class Professor(BabsonPerson):
    """"""
    def __init__(self, name, course):
        BabsonPerson.__init__(self, name)
        self.course = course

        # def __str__(self):
        #     return f"{self.name}: "

def main():
    p1 = Professor('Zhi Li', 'OIM 3640')
    print(p1)
    print(p1.id)
    print(isinstance(p1, BabsonPerson))
    print(isinstance(p1, Person))
    print(isinstance(p1, Student))
    print(isinstance(p1, Professor))


if __name__ == "__main__":
    main()
