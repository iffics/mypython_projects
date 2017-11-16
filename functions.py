#  A FUNCTION IS BLOCK OF CODE
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


# FUNCTIONS WITH RETURN TYPE

def yes_no(word: str):
    """
    A simple function which checks given word
    if at least contains one character (non empty)
    returns True else False
    :param word:
    :return: boolean
    """
    return word.isalnum()


# FUNCTION WITH SINGLE ARGUMENT AS WELL AS WITH *ARGS

def check_for_vowel(word: str, *words: str):
    """
    A simple function which checks
    whether a word starts with vowel or not.
    if yes then it will return boolean True or False
    :param word:

    """
    if word[0] in "aeiou":
        print(word + " starts with vowel")
    else:
        print(word + " Does not starts with vowel")
    if words is not None:
        for r in words:
            if r[0] in "aeiou":
                print(r + " starts with vowel")
            else:
                print(r + " Does not starts with vowel")


def check_for_vowel_word(word: str):
    """
    A simple function which checks
    whether a word starts with vowel or not.
    if yes then it will return boolean True or False
    :param word:
    :rtype: bool
    """
    return word[0] in "aeiou" or word[0] in "AEIOU"


# A SIMPLE FUNCTION WHICH TAKES A LIST RETURNS VOWEL WORDS

def filter_vowels(list: list):
    """
    A simple function which takes a list of words
    filters them and returns a list of words which
    starts from vowels.
    :param list:
    :return: list []
    """
    vowel_words = []
    for word in list:
        if check_for_vowel_word(word):
            vowel_words.append(word)
    return vowel_words


data = ["irfan", "orange", 'plan']

# CALLING ALL THE ABOVE FUNCTIONS

# greeting()
# greeting_2("irfan")
# greater_number(3, 6)

# kk('iffi', 'khan', 'kakar')
# my_sum(1, 2, 3, 4, 5, 6)

# my_func(name='tim', sport='football', roll=19)
# kkk(**my_dictionary)
# kkk(country="pakistan", match="T20")
# ky(name='iffi', age=10)

# check_for_vowel("pakistan", *data)
# print(yes_no("iffi"))

print(filter_vowels(data))
