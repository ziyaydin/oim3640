# Ex1.1

def check_fermat(a, b, c, n):
    """
    this functions checks whether Fermat's Last Theorem is correct or not
    a, b, c and n are positive integers
    n is grater than 2
    """
    if n > 2 and (a**n + b**n == c**n):
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn\' work.")

# check_fermat(1,2,3,4)
# check_fermat(3987, 4365, 4472, 12)

# Ex1.1.2


def check_fermat():
    """
    this functions checks whether Fermat's Last Theorem is correct or not
    a, b, c and n are positive integers
    n is grater than 2
    """
    a = int(input("Positive integer for a: "))
    b = int(input("Positive integer for b: "))
    c = int(input("Positive integer for c: "))
    n = int(input("Positive integer for n which is greater than 2: "))
    if n > 2 and (a**n + b**n == c**n):
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn\' work.")

# check_fermat()

# Ex1.2


def calculate_bmi(weight, height):
    """This function caclulates bmi using weight and height in metric system"""
    return float(weight/(height * height))

# print(calculate_bmi(65,1.79))


def get_bmi_category():
    """This function uses 'calculate_bmi' fucntion's result to cateogrize the bmi of people"""
    weight = float(input('What is your weight in kg:'))
    height = float(input('What is your height in meters:'))
    if calculate_bmi(weight, height) <= 18.5:
        return "Underweight"
    elif calculate_bmi(weight, height) < 25:
        return "Normal weight"
    elif calculate_bmi(weight, height) <= 29.9:
        return "Overweight"
    else:
        return "Obesity"


print(get_bmi_category())
