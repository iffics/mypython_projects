#  A FUNCTION IS BLOCK OF CODE WHICH CAN BE USED AS MANY AS YOU WANT
#  FUNCTIONS SAVE OUR TIME AND LINE OF CODE.
#  SOME FUNCTIONS TAKE ARGUMENTS AND SOME DO NOT.
#  FUNCTION TAKES INPUT AND DOES SOME WORK AND GIVES US THE OUTPUT


# simple function which goes not take any argument
def greeting():
    """
    A simple function which prints a single line.
    """
    print("Hello World!!")


# Same function with single argument
def greeting_2(name: str):
    """
    A simple function which takes one argument
    and prints it.
    :param name:
    """
    print("hello " + name)


def greater_number(number1: int, number2: int):
    """
    A simple function which takes two numbers
    and check for greater one.

    :param number1:
    :param number2:
    """
    if number1 > number2:
        print(number1, "is greater than ", number2)
    else:
        print(number2, "is greater than ", number1)


# *args allows us to pass variable number of arguments to the function.
# Let’s take an example to make this clear

def kk(*args):
    """
    A simple function which take number of arguments
    as much as you like.
    :rtype: None
    :param args:
    """
    print(*args)


def my_sum(*args):
    """
    A simple function which *args
    which means variable length arguments

    :param args:
    """
    s = 0
    for i in args:
        s += i
    print("sum is", s)


# **KWARGS ALLOW US TO PASS VARIABLE NUMBER OF KEYWORD ARGUMENT
# Like func_name(name='tim', team='school')

my_dictionary = {"name": 'irfan'}


def my_func(**kwargs):
    """
    A simple function with **kwargs
    means takes arguments as pair. name="iffi"
    :param kwargs:
    """
    for i, j in kwargs.items():
        print(i, j)


def kkk(**kwargs):
    """
    A simple function with **kwargs
    means takes arguments as pair. name="iffi"
    :param kwargs:
    """

    for k in kwargs:
        print(k, kwargs[k])


def ky(**kwargs):
    print(kwargs)


# CALLING ALL THE ABOVE FUNCTIONS
greeting()
greeting_2("irfan")
greater_number(3, 6)
kk('iffi', 'khan', 'kakar')
my_sum(1, 2, 3, 4, 5, 6)
my_func(name='tim', sport='football', roll=19)
kkk(**my_dictionary)
kkk(country="pakistan", match="T20")

ky(name='iffi', age=10)
