import math
# import math as m
# from math import pi
# from math import * # (no math prefix required to use the functions)

# use the __name__ variable to determine the name of the module i.e. if the
# module is being run directly or imported

# each module has its own namespace and thus you can define whatever global variables you want
a = 10  # accessible from elsewhere via example_module.a


def square(x):
    return x * x


def cube(x):
    return x * x * x


def circumference(r):
    return 2 * math.pi * r


def area(r):
    return math.pi * r * r


# will print the first time this module is imported
# print("hello world from example_module")
