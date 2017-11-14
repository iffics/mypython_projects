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

    time.sleep(2)
    if a == 6:
        break
