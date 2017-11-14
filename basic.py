from random import randint
from time import sleep

a = "hello "
b = "World!"
c = a + b
d = "irfan"

print(c + " " + d)

print(c * 10)

# conditional sentence boolean True and False < > == = != in keyword

a = True
b = False
print(a, b)
print(type(a), "--", type(b))

e = 0 == 0
print(e)
f = 4  # its an assignment
var = f == 4  # its equality check
g = f  # its boolean check

h = "h" in "hello"  # Searches if Found returns True else False
i = 4 < 3
j = -1 <= 0
k = 1.5 < 3
l = "w" not in "hello"  # opposite of in... if not found True & if found then false

# if else elif conditions

if 3 < 33:
    print('True')
else:
    print('No')
sis = 16
bro = 10

if sis > bro:
    print('Sis is older than bro')
else:
    print('bro is older than sis')
# And Or compound statement use and to combine 2 statements

if sis > bro and bro < sis:
    print('Compound Statement executed')
else:
    print('The Compound Statement did not work')

if sis > bro or 'h' not in "hello":
    print('Or Operator worked')
else:
    print('Or does not work')

price = 6
market = 0
market_rate = []
counter = -1
print("-----------------------")

bol = True
while bol:
    print('---')
    market = randint(1, 7)
    # market = random.randrange(steps,345,steps)

    market_rate.append(market)
    print("Current Market Rate:  ", market)

    if market_rate[-1] >= market_rate[counter]:
        diff = market_rate[-1] - market_rate[counter]
        print("Incremented by:", diff)
    else:
        diff = market_rate[counter] - market_rate[-1]
        print("Decremented by: ", diff)

    counter += 1
    sleep(2)
    if price == market:
        print("Now its time to Sell: Press Y to sell N to No:  ")
        a = str(input())
        if a == 'y' or a == 'Y':
            bol = False
