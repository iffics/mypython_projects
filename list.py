import random, time

history = []
market_rate = []
counter = -1
tst = 0
while True:

    a = random.randint(0, 7)
    print(a)
    market_rate.append(a)

    if market_rate[-1] >= market_rate[counter]:

        diff = market_rate[-1] - market_rate[counter]
        print("Incremented by:", diff)
    else:
        diff = market_rate[counter] - market_rate[-1]
        print("Decremented by: ", diff)

    counter += 1

    # time.sleep(2)
    if a == 6:
        break
print("----------------")

# SOME USEFUL LIST FUNCTIONS

testing = ['irfan', 'khan']

# testing.clear() # this will clear all the list
# testing.append() # this will add to end of the list
# testing.copy()# this will copy the entire list
# testing.count() # this is return how many times a item is in the list
# testing.extend()# this will add new list to the existing list
# testing.index('irfan')  # given an item of list will tell the index of it
# testing.pop() # will remove th last item of the list
# testing.reverse() # this is reverse the list items
# testing.sort() # this is sort the list
# testing.remove() # this is will remove the the specific item from the list
