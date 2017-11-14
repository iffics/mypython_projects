# Merging two dicts in Python 3.5+ with a single expression

# How to merge two dicts
# in Python 3.5+

x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}

# z = {**x, **y}

# print(z)


# The get() method on dicts
# and its "default" argument

name_for_userid = {
    382: "Alice",
    590: "Bob",
    951: "Dilbert",
}

def greeting(userid):
    return "Hi %s!" % name_for_userid.get(userid, "there")

greeting(382)


# Why Python is Great: Namedtuples
# Using namedtuple is way shorter than
# defining a class manually:
from  collections import namedtuple
Car = namedtuple('Car', 'color mileage')

# Our new "Car" class works as expected:
my_car = Car('red', 3812.4)
print(my_car.color)
print(my_car.mileage)
# We get a nice string repr for free:
my_car

my_car.color = 'blue'

# The standard string repr for dicts is hard to read:

my_mapping = {'a': 23, 'b': 42, 'c': 0xc0ffee}

my_mapping

# The "json" module can do a much better job:

import json

print(json.dumps(my_mapping, indent=4, sort_keys=True))

# Note this only works with dicts containing
# primitive types (check out the "pprint" module):

json.dumps({all: 'yup'})



# Why Python Is Great:
# Function argument unpacking

def myfunc(x, y, z):
    print(x, y, z)

tuple_vec = (1, 0, 1)
dict_vec = {'x': 1, 'y': 0, 'z': 1}


myfunc(*tuple_vec)

myfunc(**dict_vec)

# The lambda keyword in Python provides a
# shortcut for declaring small and
# anonymous functions:

add = lambda x, y: x + y

add(5, 3)

# You could declare the same add()
# function with the def keyword:

def add(x, y):
    return x + y
add(5, 3)

# So what's the big fuss about?
# Lambdas are *function expressions*:

(lambda x, y: x + y)(5, 3)

# → Lambda functions are single-expression
# functions that are not necessarily bound
# to a name (they can be anonymous).

# → Lambda functions can't use regular
# Python statements and always include an
# implicit `return` statement.

